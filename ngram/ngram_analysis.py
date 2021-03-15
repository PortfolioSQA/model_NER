#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 18:35:30 2021

@author: sashaqanderson
"""

import pandas as pd
df = pd.read_csv('/Users/sashaqanderson/Dropbox/USGS/ngram/NER_text.csv')

# natural language processing: n-gram ranking
import re
import unicodedata
import nltk
# add appropriate words that will be ignored in the analysis
ADDITIONAL_STOPWORDS = ['version', '3', 'keyword', 'data', 'computer', 'program', 'input', 'file', 'output', '13', '4',
                        'upw', 'package', '5', 'u', 'x', '5m', 'grid', 'mississippi', 'document', 'report', ]

import matplotlib.pyplot as plt

def basic_clean(text):
  """
  A simple function to clean up the data. All the words that
  are not designated as a stop word is then lemmatized after
  encoding and basic regex parsing are performed.
  """
  wnl = nltk.stem.WordNetLemmatizer()
  sw = nltk.corpus.stopwords.words('english') + ADDITIONAL_STOPWORDS
  text = (unicodedata.normalize('NFKD', text)
    .encode('ascii', 'ignore')
    .decode('utf-8', 'ignore')
    .lower())
  words = re.sub(r'[^\w\s]', '', text).split()
  return [wnl.lemmatize(word) for word in words if word not in sw]

words = basic_clean(''.join(str(df['Text'].tolist())))

print(words[:20])

print(pd.Series(nltk.ngrams(words, 2)).value_counts()[:20])

print(pd.Series(nltk.ngrams(words, 3)).value_counts()[:20])

bigrams_series = (pd.Series(nltk.ngrams(words, 2)).value_counts())[:20]
trigrams_series = (pd.Series(nltk.ngrams(words, 3)).value_counts())[:20]

bigrams_series.sort_values().plot.barh(color='blue', width=.9, figsize=(12, 8))

bigrams_series.sort_values().plot.barh(color='blue', width=.9, figsize=(12, 8))
plt.title('20 Most Frequently Occuring Bigrams')
plt.ylabel('Bigram')
plt.xlabel('# of Occurances')

trigrams_series.sort_values().plot.barh(color='purple', width=.9, figsize=(12, 8))

trigrams_series.sort_values().plot.barh(color='purple', width=.9, figsize=(12, 8))
plt.title('20 Most Frequently Occuring Trigrams')
plt.ylabel('Trigram')
plt.xlabel('# of Occurances')