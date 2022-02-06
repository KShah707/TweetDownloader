###################################################
# Uses the tweepy client to query a user's tweets #
###################################################

import csv
import tweepy

# Load secrets from separate file
from user_secrets import *

# Set up API client
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Fetch all tweets
with open('downloaded_tweets.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    my_tweets = [[tweet.full_text] for tweet in api.user_timeline(tweet_mode='extended')]
    print(my_tweets)
    writer.writerows(my_tweets)