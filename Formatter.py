"""
Formats images to feed into tensorflow
"""
# -*- coding: utf-8 -*-

import os
from glob import glob
import cv2
import numpy as np
import config as cfg

FOLDER = './output/generated'
TRAIN_DATA = './output/training_data.npy'
TRAIN_LABELS = './output/training_labels.npy'
TEST_DATA = './output/testing_data.npy'
TEST_LABELS = './output/testing_labels.npy'

def read_images():
    return [file for file in glob(FOLDER + '/**/*.bmp', recursive=True)]
# end if


def save_separated(images, data_file, label_file):
    data = []
    labels = []
    for img in images:
        # add label
        label = img.split(os.sep)[-2]
        labels.append(label)
        # read and flatten image
        image = cv2.imread(img, 0)
        data.append(image.flatten())
    # end for
    np.save(data_file, np.array(data))
    np.save(label_file, np.array(labels))
# end function


def test_integrity():
    # training labels
    labels = np.load(TRAIN_LABELS);
    train = dict()
    for x in labels:
        if x in train:
            train[x] += 1
        else:
            train[x] = 1
    # end for
    print("Training labels:", len(train.keys()))

    # testing labels
    labels = np.load(TEST_LABELS);
    test = dict()
    for x in labels:
        if x in test:
            test[x] += 1
        else:
            test[x] = 1
    # end for
    print("Testing labels:", len(test.keys()))

    # check
    if len(train.keys()) == len(test.keys()):
        print("Integrity check OK.")
    else: 
        print("Integrity check FAILED.")
    # end if
# end function


def format_docs():
    # get all image files
    images = np.array(read_images())
    # suffle them
    np.random.shuffle(images)
    # separate training and testing
    pos = int(len(images) * cfg.DATASET_RATIO)
    training = images[:pos]
    testing = images[pos:]
    # a little printout
    print("Total images:", len(images))
    print("Training:", len(training))
    print("Testing:", len(testing))
    # separate labels and image data
    save_separated(training, TRAIN_DATA, TRAIN_LABELS)
    save_separated(testing, TEST_DATA, TEST_LABELS)
    print("Formatting done.")
    test_integrity();
# end if
