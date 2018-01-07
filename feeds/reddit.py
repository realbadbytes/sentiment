# Reddit API feed

import praw
import sys
import os

def main():
    if os.getenv("REDDIT_CLIENT_ID") is None:
        print "Set your Reddit environment variables:"
        print "REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET"
        sys.exit()
    client_id = os.environ['REDDIT_CLIENT_ID']
    client_secret = os.environ['REDDIT_CLIENT_SECRET']
    try:
        reddit_api = praw.Reddit(client_id = client_id,
                        client_secret = client_secret,
                        user_agent = "sentiment")
    except:
        print "Reddit auth failed."
        sys.exit()
    sub = raw_input("Subreddit: ")
    keyword = raw_input("Keyword: ")
    get_posts(keyword, sub, reddit_api)

# currently only dumps top 10 posts from subreddit
# regardless of keyword
def get_posts(keyword, sub, reddit_api):
    for post in reddit_api.subreddit(sub).hot(limit=10):
        print post.title

if __name__ == '__main__':
    main()
