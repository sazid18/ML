# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 19:17:04 2018

@author: MARK
"""

import os
from sklearn import *
from collections import Counter
import pandas as pd
import numpy as np
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import _pickle as c


def load(clf_file):
    with open(clf_file,"rb") as fp:
        clf = c.load(fp)
    return clf


def make_dict():
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    words = []
   
    for email in emails:
        f = open(email, errors = 'ignore')
        blob = f.read()
        words += blob.split(" ")
        

    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)


clf = load("text_classifier.mdl")
d = make_dict()

while True:
    features = []
    inp = input(">").split()
    if inp[0] == "exit":
        break
    for word in d:
        features.append(inp.count(word[0]))
    res = clf.predict([features])
    print (["Spam!", "Not Spam!"][res[0]])    
    
    
    
    