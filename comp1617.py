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
dataset16 = pd.read_csv('2016.csv')
dataset17 = pd.read_csv('2017.csv')

print("The Dataset for 2016: ",dataset16)
print("The Dataset for 2017: ",dataset17)

print("Dataset Length for 2016:",len(dataset16))
print("Dataset Length for 2017:",len(dataset17))

X16_train = dataset16.iloc[:, :-1].values
y16_train = dataset16.iloc[:, 8].values
X17_test = dataset17.iloc[:, :-1].values
y17_test = dataset17.iloc[:, 8].values

# Splitting the dataset into the Training set and Test set
#from sklearn.cross_validation import train_test_split
#X15_train, X15_test, y15_train, y15_test = train_test_split(X15, y15, test_size = 0.2, random_state = 0)

print("Independent Training set: ",X16_train)
print("Independent Testing set: ",X17_test)
print("Dependent Training set: ",y16_train)
print("Dependent Testing set: ",y17_test)

print("Training set length: ",len(X16_train))
print("Testing set length: ",len(X17_test))

#Fit multiple linear regresion to the data
from sklearn.linear_model import LinearRegression
regressor15 = LinearRegression()

regressor15.fit(X16_train,y16_train)


#Predicting the test result
y17_pred = regressor15.predict(X17_test)

for index in range(len(y17_pred)):
    iter=index+1
    print ("Predictions #",iter,":", y17_pred[index], "\t\tActual #",iter,":",y17_test[index])


   
"""for index in range(len(y17_pred)):
iter=index+1
print ("Predictions 15 #",iter,":", y15_pred[index], "\tPredictions 16 #",iter,":", y16_pred[index],"\tPredictions 17 #",iter,":", y17_pred[index])
"""


