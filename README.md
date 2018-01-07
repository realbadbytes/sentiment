Requirements:

sudo pip install tweepy requests[security] matplotlib termcolor nytimesarticle praw

------------------------------------------------------

To use the two existing feeds, you need your own API keys for Twitter
and the New York Times. Get your keys here:

Twitter: https://dev.twitter.com/resources/signup#

NYT: https://developer.nytimes.com/signup

Reddit: https://www.reddit.com/wiki/api

Export all API keys to your environment (place in ~/.bashrc):

------------------------------------------------------

export NYTIMES_KEY="your key"

export TWITTER_CKEY="your ckey"

export TWITTER_CSEC="your csec"

export TWITTER_ATOK="your atok"

export TWITTER_ASEC="your asec"

export REDDIT_CLIENT_ID="your client_id"

export REDDIT_CLIENT_SECRET="your client_secret"
