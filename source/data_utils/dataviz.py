#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt


def implot(img, label):
    """
    Show and image with a label
    """
    plt.imshow(img)
    plt.xlabel(label)
    plt.show()


def implotr(imgs, lbls, labels, r):
    """
    Plot r images with corresponding labels
    """
    plt.figure(figsize=(10, 10))
    for i in range(r):
        plt.subplot(5, 5, i+1)
        plt.imshow(imgs[i], cmap=plt.cm.binary)
        plt.grid(False)
        plt.xlabel(labels[lbls[i]])
    plt.subplots_adjust(hspace=0.2)
    plt.show()


def implot_colorbar(img, label):
    plt.imshow(img)
    plt.grid(False)
    plt.xlabel(label)
    plt.show()