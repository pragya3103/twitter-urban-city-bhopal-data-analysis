# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:39:02 2021

@author: pragyaja
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import warnings


from textblob import TextBlob

polarity = []

for i in hindi['Translated_to_english']:
    x = TextBlob((i))
    polarity.append(x.polarity)
    
    
hindi['polarity'] = polarity

tweet = TextBlob(str(english['full_text']))


english['full_text'].isnull().any()

from sklearn.feature_extraction.text import CountVectorizer



tweet.polarity

cv = CountVectorizer(stop_words = 'english')
words = cv.fit_transform(weetweet)


