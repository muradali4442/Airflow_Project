import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


def twitter():
   
    
    access_key = ""             #here you have to put your own generated keys
    access_secret = ""
    consumer_key = ""
    consumer_secret = ""
    

    # Authentication from twitter
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)

    # API
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name='@dummy',
                               # 200 is the maximum allowed count
                               count=200,
                               include_rts=True,
                               # Necessary to keep full_text
                               # otherwise only the first 140 words are extracted
                               tweet_mode='extended'
                               )

    list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                         'text': text,
                         'favorite_count': tweet.favorite_count,
                         'retweet_count': tweet.retweet_count,
                         'created_at': tweet.created_at}

        list.append(refined_tweet)

    df = pd.DataFrame(list)
    df.to_csv('refined_tweets.csv')


