# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:02:19 2019

@author: Ballerina
"""

from get_tweets_list import _getTweets

tweets = []
tweets = _getTweets(query = "PewDiePie", count = 100)
target = open("Data_files/tweets_batch1.txt",  "a", encoding='utf-8')

for tweet in tweets:
    
    if tweet is not None:
        target.write(tweet)
        target.write('\n')