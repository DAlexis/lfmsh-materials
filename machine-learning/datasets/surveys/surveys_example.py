#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 09:52:39 2021

@author: dalexies
"""

import pandas as pd
import numpy as np

data_frame = pd.read_csv("responses.csv")


from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import scale
from sklearn.metrics import classification_report
import sklearn.metrics
import matplotlib.pyplot as plt

personal = ["Age","Height","Weight","Number of siblings"]
music_preferences = ["Pop","Rock","Metal or Hardrock","Punk","Hiphop, Rap","Reggae, Ska","Swing, Jazz","Rock n roll","Alternative","Latino","Techno, Trance","Opera"]
cinema_preferences = ["Movies","Horror","Thriller","Comedy","Romantic","Sci-fi","War","Fantasy/Fairy tales","Animated","Documentary","Western","Action"]
spending = ["Spending on looks","Spending on gadgets","Spending on healthy eating"]
phobias = ["Flying","Storm","Darkness","Heights","Spiders","Snakes","Rats","Ageing","Dangerous dogs","Fear of public speaking"]
interests = ["History","Psychology","Politics","Mathematics","Physics","Internet","PC","Economy Management","Biology","Chemistry","Reading","Geography","Foreign languages","Medicine","Law"]

target_columns = cinema_preferences + music_preferences + phobias
output_column = "Gender"

partial_data = data_frame[target_columns + [output_column]].dropna()
lines_count = len(partial_data)

partial_data = partial_data.sample(frac=1.0, random_state=1234)

X = np.array(partial_data[target_columns].values)
y = partial_data[output_column].values

train_part = 0.8
train_lines = int(lines_count * train_part)

X_train = X[:train_lines, :]
y_train = y[:train_lines]


X_val = X[train_lines:, :]
y_val = y[train_lines:]

# clf = DecisionTreeClassifier()
# clf = KNeighborsClassifier(n_neighbors=51)
# clf = KNeighborsClassifier(n_neighbors=5)
# clf = RandomForestClassifier()
# clf = LogisticRegression()
clf = SVC()
clf.fit(X_train, y_train)

y_predict = clf.predict(X_val)
    
print(classification_report(y_val, y_predict))#, target_names=["female", "male"]))
print(sklearn.metrics.confusion_matrix(y_val, y_predict))
