#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:40:43 2016

@author: ignacio
"""
import pandas as pd
from scipy import spatial
from scipy.stats import spearmanr

file = "../Tensorflow/basic_w2v.txt"
#file = "../Gensim/gensim_word2vec.txt"
word_vector = pd.read_table(file, header = None, sep = " ")

word_vector_dict = dict((word,key) for key,word in enumerate(word_vector[0]))


file = "../MEN/MEN_dataset_lemma_form_full"
men = pd.read_table(file, header = None, sep = " ", names=['word1', 'word2', 'score'])

def CosSim(word1,word2):
    try:
        key1 = word_vector_dict[word1]
        v1 = word_vector.iloc[key1][1:]
        key2 = word_vector_dict[word2]
        v2 = word_vector.iloc[key2][1:]
        return float(1 - spatial.distance.cosine(v1,v2))
    except:
        return 'NA'
        
score = []
for index,row in men.iterrows():
    score.append(CosSim(row.word1[:-2],row.word2[:-2]))

print(spearmanr(score,men.score))