#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("/home/leonardo/Udacity Machine learning/tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("/home/leonardo/Udacity Machine learning/final_project/final_project_dataset.pkl", "r") )

### remove the "TOTAL" outlier
data_dict.pop('TOTAL', 0)
ta_dict.pop('total', 0)