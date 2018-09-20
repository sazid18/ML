# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:06:41 2018

@author: MARK
"""

import os
import pandas as pd
import numpy as np
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import _pickle as c


def save(clf, name):
    with open(name, 'wb') as fp:
        c.dump(clf, fp)
    print ("saved")

def make_dict():
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    words = []
    c = len(emails)
    for email in emails:
        f = open(email, errors='ignore')
        rd = f.read()
        words += rd.split(' ')
        

    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
    return (dictionary.most_common(3000))

def make_dataset(dictionary):
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    features_set = []
    labels = []
    for email in emails:
        data = []
        f = open(email, errors = 'ignore')
        words = f.read().split(' ')
        for key in dictionary:
            data.append(words.count(key[0]))
        features_set.append(data)
        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)
    
    return features_set,labels
    

d = make_dict()
features , labels = make_dataset(d)

x_train, x_test, y_train, y_test = tts(features,labels,test_size=0.2)
clf = MultinomialNB()
clf.fit(x_train,y_train)

pred = clf.predict(x_test)
print (accuracy_score(y_test,pred))
save(clf,"text_classifier.csv")


    


   