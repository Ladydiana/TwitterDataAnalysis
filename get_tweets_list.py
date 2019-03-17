# -*- coding: utf-8 -*-
#General

import tweepy
from tweepy import OAuthHandler


#Keeping these a secret for the github repo
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''


# create OAuthHandler object
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# set access token and secret
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# create tweepy API object to fetch tweets
api = tweepy.API(auth)


def _getTweets(query, count=500):
    
    tweets = [] #storage container for the tweets
    tweet = []
    #target = open("Data_files/tweets_batch1.txt",  "w")
    query = str(query + "  -filter:retweets")
    
    for tweet_info in tweepy.Cursor(api.search, q=query, lang = 'en', tweet_mode='extended').items(count):
        if 'retweeted_status' in dir(tweet_info):
            tweet=tweet_info.retweeted_status.full_text
        else:
            tweet=tweet_info.full_text
        tweets.append(tweet)        
    
    return tweets


        
    
'''
    #Kept for future reference in case needed
    #Removed as we couldn't retrieve full text with this
    fetched_tweets = api.search(q, count = count, lang="en", rpp=1, show_user = 'False')
    
    print(len(fetched_tweets))
    
    for tweet in fetched_tweets:
        parsed_tweet = {} #empty dictionary to store tweet data
        parsed_tweet['text'] = tweet.text
        if "http"not in tweet.text:
            #line = re.sub("RT ", " ", tweet.text)
            line = re.sub("[^A-Za-z]", " ", tweet.text)
            target.write(line+"\n")
    ''' 