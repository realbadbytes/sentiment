# New York Times API feed

from nytimesarticle import articleAPI
from termcolor import colored
import requests
import os
import sys
import json
import time
import sched

keyword = raw_input("Enter keyword to search NY Times articles:\n")
today = time.strftime('%Y%m%d')

def parse_headlines(keyword, api):
    articles = api.search(q=keyword,
        fq={'headline':keyword, 'source':['Reuters','AP', 'The New York Times']}, begin_date=today)
    headlines = []
    for a in articles['response']['docs']:
        result = {}
        result['headline'] = a['headline']['print_headline'].encode("utf8")
        result['web_url'] = a['web_url'].encode('utf8')
        headlines.append(result)
    return headlines

def print_headlines(headlines):
    #print keyword + " headlines " + today + '\n'
    for headline in headlines:
        print colored(headline['headline'], 'red')
        print headline['web_url'] + '\n'

def main():
    if os.getenv('NYTIMES_KEY') is None:
        print "Usage: \nSet 1 environment variable for NY Times authentication: "
        print "export NYTIMES_KEY=\"your key\""
        sys.exit()
    # auth to NY Times
    s = sched.scheduler(time.time, time.sleep)
    api = articleAPI(os.environ['NYTIMES_KEY'])
    # parse and print headlines
    sys.stdout.flush()
    headlines = parse_headlines(keyword, api)
    print_headlines(headlines)
    while True:
        for i in xrange(10, 0, -1):
            sys.stdout.flush()
            sys.stdout.write('Refresh in %d\r' % i)
            time.sleep(1)
        sys.stdout.flush()
        headlines = parse_headlines(keyword, api)
        print_headlines(headlines)

if __name__ == '__main__':
    main()
