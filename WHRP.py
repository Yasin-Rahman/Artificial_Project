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
url="https://raw.githubusercontent.com/Yasin-Rahman/CSV/master/2015.csv"
s=requests.get(url).content
dataset=pd.read_csv(io.StringIO(s.decode('utf-8')))
dataset = pd.read_csv(url)"""

# Importing the dataset
dataset = pd.read_csv('2015.csv')
print("The Dataset",dataset)
print("Dataset Length",len(dataset))
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 8].values

print("Independent array of Variables",X)
print("Dependent array of Variables",y)

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
print("Independent Training set: ",X_train)
print("Independent Testing set: ",X_test)
print("Dependent Training set: ",y_train)
print("Dependent Testing set: ",y_test)

print("Training set length: ",len(X_train))
print("Training set length: ",len(X_test))


#Fit multiple linear regresion to the data
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

#Predicting the test result
y_pred = regressor.predict(X_test)
print("Predicted array of attributes",y_pred)

for index in range(len(y_pred)):
   iter=index+1
   print ("Predictions #",iter,":", y_pred[index], "\tActual #",iter,":",y_test[index])


