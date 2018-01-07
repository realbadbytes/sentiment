# Twitter API feed

from termcolor import colored
import warnings
import json
import matplotlib.pyplot as plt
from operator import itemgetter
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from httplib import IncompleteRead
import time
import os
import sys

keywords = ['handshake', 'climate', 'climate change', 'paris', 'germany', 'paris accord', 'hair', 'russia', 'comey']
keyword_count = 0
processed_count = 0
tweets = []
plot_data = []
detected_tweets = []

class StdOutListener(StreamListener):

    def on_data(self, data):
        # fix OOM issue
        global processed_count
        processed_count += 1
        if len(tweets) > 50000:
            reset()
        data = json.loads(data)
        if 'text' in data: 
            tweets.append(data)
            # detect duplicates
            if data['text'] in detected_tweets:
                return
            for target in keywords:
                if target in data['text']:
                    print colored("Tweet: %s" % data['text'], 'red')
                    detected_tweets.append(data['text'])
                    global keyword_count
                    keyword_count += 1
                    print "[+] Tweets processed: %d" % processed_count
        return True
    
    def on_error(self, status):
        print "[-] Error: %d" % status

def reset():
    global tweets
    global keyword_count
    tweets = []
    keyword_count = 0

def auth(consumer_key, consumer_secret, access_token, access_secret):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def main():
    if os.getenv("TWITTER_CSEC") is None:
        print "\nUsage: \nSet 4 environment variables for Twitter authentication:"
        print "export TWITTER_CKEY=\"your ckey\"\n" \
            "export TWITTER_CSEC=\"your csec\"\n" \
            "export TWITTER_ATOK=\"your atok\"\n" \
            "export TWITTER_ASEC=\"your asec\"\n"
        sys.exit()

    # get auth tokens from environment
    ckey = os.environ['TWITTER_CKEY']
    csec = os.environ['TWITTER_CSEC']
    atok = os.environ['TWITTER_ATOK']
    asec = os.environ['TWITTER_ASEC']

    listener = StdOutListener()
    print "Authenticating to Twitter"
    api = auth(ckey, csec, atok, asec)
    keyword = raw_input("Enter keyword for live tweet dump:\n")
    print "Searching tweets about %s for %s" % (keyword, tuple(keywords))
    stream = Stream(api, listener)
    stream.filter(track=[keyword])

if __name__ == '__main__':
    main()
