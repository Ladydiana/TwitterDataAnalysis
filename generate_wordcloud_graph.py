# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:25:28 2019

@author: Culincu Diana Cristina
"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re




def generate_graph(fname):
    with open(fname, encoding='utf-8') as f:
        content = f.readlines()
        
    content = ''.join(content)
    content = re.sub("[^A-Za-z]", " ", content)
    #print(content)
    stopwords = set(STOPWORDS)
    
    wordcloud = WordCloud(background_color="white", stopwords=stopwords, width=1200, height=1000, normalize_plurals=True, collocations=False)
    wordcloud.generate(content)
    
    plt.figure( figsize=(20,10), facecolor='k')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title("Testing wordcloud")
    
generate_graph("Data_files/tweets_batch3_cleaned.txt")  