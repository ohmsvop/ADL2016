#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:46:32 2016

@author: ignacio
"""

from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.Text8Corpus('../Corpus/text8')

model = word2vec.Word2Vec(sentences, size=500, window=25)


f = open("../fullVocab.txt").read()
vocabulary = f.split()
output = open("gensim_word2vec.txt","w")

for word in vocabulary:
    try:
        model[word]
        output.write(word+" ")
        output.write(" ".join(str(x) for x in model[word]))
        output.write("\n")
    except:
        pass
output.close()
    