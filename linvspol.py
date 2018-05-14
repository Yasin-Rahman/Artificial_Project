# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:56:43 2018

@author: Shreshto
"""

#Multiple Linear Regression
# Data Preprocessing Template

# Importing the libraries


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


"""#For online import
import io
import requests
url15="https://raw.githubusercontent.com/Yasin-Rahman/CSV/master/2015.csv"
s15=requests.get(url15).content
dataset15=pd.read_csv(io.StringIO(s15.decode('utf-8')))
#dataset15 = pd.read_csv(url15)
"""

# Importing the dataset
dataset15 = pd.read_csv('2015.csv')

print("The Dataset for 2015: ",dataset15)

print("Dataset Length for 2015:",len(dataset15))

X15 = dataset15.iloc[:, :-1].values
y15 = dataset15.iloc[:, 8].values

print("Independent array of Variables",X15)
print("Dependent array of Variables",y15)

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X15_train, X15_test, y15_train, y15_test = train_test_split(X15, y15, test_size = 0.2, random_state = 0)

print("Independent Training set: ",X15_train)
print("Independent Testing set: ",X15_test)
print("Dependent Training set: ",y15_train)
print("Dependent Testing set: ",y15_test)

print("Training set length: ",len(X15_train))
print("Testing set length: ",len(X15_test))

#Fit multiple linear regresion to the data
from sklearn.linear_model import LinearRegression
regressor15 = LinearRegression()

regressor15.fit(X15_train,y15_train)

from sklearn.preprocessing import PolynomialFeatures
pol_reg = PolynomialFeatures(degree=2)
X_pol = pol_reg.fit_transform(X15_train)
X_pol_test = pol_reg.fit_transform(X15_test)
regressor15_2 = LinearRegression()
regressor15_2.fit(X_pol,y15_train)

#Predicting the test result
y15_pred = regressor15.predict(X15_test)
y15_pred_pol = regressor15_2.predict(X_pol_test)
print("Predicted array of attributes",y15_pred)

for index in range(len(y15_pred)):
    iter=index+1
    print ("Predictions Linear#",iter,":", y15_pred[index], "\tActual #",iter,":",y15_test[index])
    
for index in range(len(y15_pred_pol)):
    iter=index+1
    print ("Predictions Polynomial#",iter,":", y15_pred_pol[index], "\t\tActual #",iter,":",y15_test[index])
    
for index in range(len(y15_pred)):
    iter=index+1
    print ("Predictions pol #",iter,":", y15_pred_pol[index], "\t\tprediction linear #",iter,":",y15_pred[index])


   
"""for index in range(len(y17_pred)):
iter=index+1
print ("Predictions 15 #",iter,":", y15_pred[index], "\tPredictions 16 #",iter,":", y16_pred[index],"\tPredictions 17 #",iter,":", y17_pred[index])
"""


