#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import numpy as np
sys.path.append("/home/leonardo/Udacity Machine learning/tools/")
from time import time
from email_preprocess import preprocess

from sklearn import svm 


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

""" features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100] """

clf = svm.SVC(kernel='rbf', C=10000)
### train the classifier using the features and labels 
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"


### predict the rest of the data 
t0 = time()
prediction = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

### check for accuracy 
print "accuracy", clf.score(features_test, labels_test)
print prediction[10]
print prediction[26]
print prediction[50]
print len(prediction)
print np.count_nonzero(prediction == 1)
print (prediction == 1).sum()
