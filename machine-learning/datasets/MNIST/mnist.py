#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 23:55:03 2021

@author: dalexies
"""

import mnist_loader

import numpy as np
from sklearn.tree import DecisionTreeClassifier
import sklearn.metrics
import matplotlib.pyplot as plt

train_images, train_labels = mnist_loader.load_mnist_train()
test_images, test_labels = mnist_loader.load_mnist_test()

pixels_count = train_images.shape[1] * train_images.shape[2]

num_train = train_images.shape[0]
train_X = train_images.reshape((num_train, pixels_count))

num_test = test_images.shape[0]
test_X = test_images.reshape((num_test, pixels_count))

clf = DecisionTreeClassifier(random_state=1234)
clf.fit(train_X, train_labels)

predictions = clf.predict(test_X)

error_indexes = []
for i in range(len(test_labels)):
    if test_labels[i] != predictions[i]:
        error_indexes.append(i)

mnist_loader.plot_mnist(error_indexes[0], test_images, predictions)
mnist_loader.plot_mnist(error_indexes[1], test_images, predictions)
mnist_loader.plot_mnist(error_indexes[2], test_images, predictions)
mnist_loader.plot_mnist(error_indexes[3], test_images, predictions)
