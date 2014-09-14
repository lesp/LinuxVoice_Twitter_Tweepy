import tweepy
from time import sleep
import sys

consumer_key = "YOUR API KEY"
consumer_secret = "YOUR API SECRET"
access_token = "YOUR TOKEN"
access_token_secret = "YOUR TOKEN SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
    sleep(5)