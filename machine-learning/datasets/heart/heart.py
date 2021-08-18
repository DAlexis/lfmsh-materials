#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:37:55 2021

@author: dalexies
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import scale
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
import sklearn.metrics
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler

data_frame = pd.read_csv("heart.csv")

positive = data_frame[data_frame["target"] == 1]
negative = data_frame[data_frame["target"] == 0]

# data_frame.plot.scatter(x="trestbps", y="thalach", c="target", colormap='viridis')

data_frame["cp_0"] = data_frame["cp"] == 0
data_frame["cp_1"] = data_frame["cp"] == 1
data_frame["cp_2"] = data_frame["cp"] == 2
data_frame["cp_3"] = data_frame["cp"] == 3

# data_frame = data_frame.drop(columns=["cp"])

data_frame["thal_0"] = data_frame["thal"] == 0
data_frame["thal_1"] = data_frame["thal"] == 1
data_frame["thal_2"] = data_frame["thal"] == 2
data_frame["thal_3"] = data_frame["thal"] == 3


data_frame = data_frame.drop(columns=["cp", "thal"])
data_frame = data_frame.sample(frac=1, random_state=1234).dropna()

train_part = 0.8

train_size = int(len(data_frame) * train_part)

train_set = data_frame.iloc[:train_size, :]
val_set = data_frame.iloc[train_size:, :]

train_y = train_set["target"].values
train_X = train_set.drop(columns=["target"]).values

val_y = val_set["target"].values
val_X = val_set.drop(columns=["target"]).values


scaler = StandardScaler()
scaler.fit(train_X)

train_X = scaler.transform(train_X)

# clf = DecisionTreeClassifier(random_state=1234)
# clf = KNeighborsClassifier(n_neighbors=3)
# clf = RandomForestClassifier()
clf = LogisticRegression()
# clf = Perceptron(penalty="l2", alpha=0.0003, tol=1e-4, random_state=1234)
# clf = MLPClassifier(solver='adam', alpha=1e-4,
#                       hidden_layer_sizes=(10, 10, 10, 10), random_state=0, max_iter=1000)
# clf = SVC()
clf.fit(train_X, train_y)

val_X = scaler.transform(val_X)
predicted_y = clf.predict(val_X)

print(classification_report(val_y, predicted_y))#, target_names=["female", "male"]))
print(sklearn.metrics.confusion_matrix(val_y, predicted_y))

# print(list(zip(list(data_frame.columns), clf.coef_[0].tolist())))

features_to_plot_scatter = ["age", "trestbps", "chol", "thalach", "oldpeak", "slope"]

features_to_plot_count = len(features_to_plot_scatter)

positive = data_frame[data_frame["target"] == 1]
negative = data_frame[data_frame["target"] == 0]


fig, axs = plt.subplots(features_to_plot_count, features_to_plot_count)
for i in range(features_to_plot_count):
    for j in range(features_to_plot_count):
        axs[i, j].scatter(positive[features_to_plot_scatter[i]], positive[features_to_plot_scatter[j]], s=1)
        axs[i, j].scatter(negative[features_to_plot_scatter[i]], negative[features_to_plot_scatter[j]], s=1)
fig.tight_layout(pad=0.1)

#chol_positive = data_frame[data]