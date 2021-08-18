import gzip
import numpy as np

import matplotlib.pyplot as plt

image_size = 28

def load_images(filename, num_images):
    f = gzip.open(filename, 'r')
    f.read(16)
    buf = f.read(image_size * image_size * num_images)
    
    data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    data = data.reshape(num_images, image_size, image_size, 1)
    
    return data


def load_labels(filename, num_labels):
    f = gzip.open(filename,'r')
    f.read(8)
    labels = []
    for i in range(0,num_labels):   
        buf = f.read(1)
        labels.append(np.frombuffer(buf, dtype=np.uint8).astype(np.int64)[0])
    return labels
        

def load_mnist_train():
    num_images = 60000
    return load_images('train-images-idx3-ubyte.gz', num_images), load_labels('train-labels-idx1-ubyte.gz', num_images)


def load_mnist_test():
    num_images = 10000
    return load_images('t10k-images-idx3-ubyte.gz', num_images), load_labels('t10k-labels-idx1-ubyte.gz', num_images)


def plot_mnist(index, data, labels=None):
    image = np.asarray(data[index]).squeeze()
    if labels is not None:
        plt.title("Digit %d" % labels[index])
    plt.imshow(image)
    