#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 15:37:16 2021

@author: dalexies
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import scale
from sklearn.metrics import classification_report
import sklearn.metrics
import matplotlib.pyplot as plt

data_frame = pd.read_csv("student-mat.csv")

w_alk = data_frame["Walc"].values
health = data_frame["health"].values

x = np.asarray(w_alk) + np.random.normal(0, 0.1, size=(len(w_alk)))
y = np.asarray(health) + np.random.normal(0, 0.2, size=(len(health)))

#data_frame["Walc"]

