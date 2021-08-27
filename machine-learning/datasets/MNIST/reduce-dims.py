#!/usr/bin/env python3

import mnist_loader

import numpy as np
from sklearn.tree import DecisionTreeClassifier
import sklearn.metrics
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

train_images, train_labels = mnist_loader.load_mnist_train()

pixels_count = train_images.shape[1] * train_images.shape[2]

num_train = train_images.shape[0]
train_X = train_images.reshape((num_train, pixels_count))


random_indices = np.random.choice(len(train_X), size=5000, replace=False)

train_X = train_X[random_indices]
train_labels = np.asarray(train_labels)[random_indices]

# transformer = PCA(n_components=2)
transformer = TSNE()
reduced = transformer.fit_transform(train_X)

for i in range(10):
    this_digits = reduced[train_labels == i]
    plt.scatter(this_digits[:, 0], this_digits[:, 1], s=30, marker="$%d$" % i)
