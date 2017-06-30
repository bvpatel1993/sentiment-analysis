from apscheduler.schedulers.blocking import BlockingScheduler

import tweepy, sys, json
import re
reload(sys)
sys.setdefaultencoding("utf-8")

consumer_key = 'kSASEcTGMr44q3iyr2827OS9v'
consumer_secret = 'ncWvAjv4L49sFSDtKHGiRhJdWZ1ohdYeUeWor2rh2PMDxM11aq'
access_token_key = '834284345795964928-jT8SaAsE4sTT7W4Sb3ddZ2c9H0uMwbH'
access_token_secret = 'W8wO9VV7T2lgZNyZI4siJEGZVCdIpzxoqpbCUDeiOMPuc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
myApi = tweepy.API(auth)

def tweet_collection():
    geo = "37.3382,-121.8863,100mi"
    tweets = myApi.search(q="Miley Cyrus", count=1000)
    for tweet in tweets:
        print tweet.created_at, tweet.user.screen_name, tweet.text
        String=tweet.text
        with open("raw_data/san_jose.txt", 'a+') as files:
           files.write(String)
           files.write("\n")
scheduler = BlockingScheduler()
scheduler.add_job(tweet_collection, 'interval', seconds=30)
scheduler.start()