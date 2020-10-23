#!/usr/bin/python

from time import time
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn import neighbors, ensemble

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################

### KN Neighbors
clf = neighbors.KNeighborsClassifier(n_neighbors=15, weights='distance')

### train the classifier using the features and labels 
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

### predict the rest of the data 
t0 = time()
clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

### check for accuracy 
print "accuracy", clf.score(features_test, labels_test)

################################################################################

### ADABOOST
""" clf = ensemble.AdaBoostClassifier(n_estimators=100, learning_rate=.1)

### train the classifier using the features and labels 
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

### predict the rest of the data 
t0 = time()
clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

### check for accuracy 
print "accuracy", clf.score(features_test, labels_test) """

################################################################################

### RANDOM FOREST
""" clf = ensemble.RandomForestClassifier(n_estimators=100, min_samples_leaf=50, criterion='entropy')
 
### train the classifier using the features and labels 
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

### predict the rest of the data 
t0 = time()
clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

### check for accuracy 
print "accuracy", clf.score(features_test, labels_test)  """


try:
    prettyPicture(clf, features_test, labels_test, "test")
except NameError:
    pass
