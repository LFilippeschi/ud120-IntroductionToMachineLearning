#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math 

enron_data = dict(pickle.load(open("/home/leonardo/Udacity Machine learning/final_project/final_project_dataset.pkl", "rb")))

print 'Features of each datapoint: '
print(len(enron_data['TAYLOR MITCHELL S']))

### Total number of POI in the dataset 
print 'Total number of POI in the dataset: ' 
count = 0
for x in enron_data:
    if enron_data[x]['poi'] == 1:
        count += 1
print count

print 'Prentice James Total stock value: '
print enron_data['PRENTICE JAMES']['total_stock_value']

print 'Colwell Wesley emails to POI: '
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print 'Skilling Jeffrey K exercised stock options: '
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print 'Total payments of directors: '
print enron_data['FASTOW ANDREW S']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['SKILLING JEFFREY K']['total_payments']
#print enron_data.keys()

print 'Total number of datapoints without a salary entry: '
count = 0
for person in enron_data:
    if not math.isnan(float(enron_data[person]['salary'])):
        count += 1
print count

print 'Total number of datapoints without an email address: '
count = 0
for person in enron_data:
    if not enron_data[person]['email_address'] == 'NaN':
        count += 1
print count

print 'Total number of datapoints without total_payments: '
count = 0
for person in enron_data:
    if enron_data[person]['total_payments'] == 'NaN':
        count += 1
print count

print 'percentage: '
print float(float(21)/(21+125))

print 'Total number of POIs without total_payments: '
count = 0
for person in enron_data:
    if enron_data[person]['total_payments'] == 'NaN' and enron_data[person]['poi'] == True:
        count += 1
print count
