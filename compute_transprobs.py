# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:43:07 2024

@author: ifrommer
"""
import pandas as pd

def compute_transprobs(sequence, prefix_len, suffix_len):
    """  Returns n-gram transition probability matrix.
      Supply the sequence, desired prefix_len and suffix_len.
    """
    n = prefix_len;               s = suffix_len;     # aliases
    SEQ_LEN = len(sequence)
    prefixes = [sequence[i:i+n] for i in range(0,SEQ_LEN-n)]   
    suffixes = [sequence[i:i+s] for i in range(n,SEQ_LEN-s+1)]

    # pd.crosstab didn't like tuples, so made ngram labels into strings
    pf = ['_'.join(x) for x in prefixes]
    sf = ['_'.join(x) for x in suffixes]

    transprobs = pd.crosstab(pf[:len(sf)],sf,normalize='index')
    return transprobs 

# main
sequence = ['a', 'd', 'a', 'e', 'c', 'd', 'd', 'b']
n = 1   # change this to try it out
s = 3   #  "

transprobs = compute_transprobs(sequence, n, s)
print(transprobs)
""" to reverse the stringing of the ngrams, do something like:
     ngram_as_tuple = transprobs.index[i].split('_')
      or transprobs.columns[j].split('_') where i, j are row, col # rspctvly
"""

#%%  development code
"""
import random

symbols = ['a','b','c','d','e']

LEN = 8

def get_n_grams(froms,n):
    n_grams = [froms[i:i+n] for i in range(0,len(froms)-n)]
    return n_grams

tos = random.choices(symbols,k=LEN)
froms = [symbols[0]] + tos[0:-1]    # the prior "to" but pad beginning w/ a symbol
# history = list(zip(froms,tos))


n = 1
s = 1

prefixes = get_n_grams(froms,n)
suffixes = froms[n:]

suffixes2 = [froms[i:i+s] for i in range(n,LEN-s+1)]


pf = ['_'.join(x) for x in prefixes]
sf = ['_'.join(x) for x in suffixes2]

trans_counts = pd.crosstab(pf[:len(sf)],sf,normalize='index')
print(trans_counts)

#print(prefixes)
#print(suffixes2)
"""


