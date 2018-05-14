# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:56:43 2018

@author: Shreshto
"""

#Multiple Linear Regression
# Data Preprocessing Template

# Importing the libraries

def run():
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
    print("<br>")
    print("<br>")

    print("Dataset Length for 2015:",len(dataset15))
    print("<br>")
    print("<br>")

    X15 = dataset15.iloc[:, :-1].values
    y15 = dataset15.iloc[:, 8].values

    print("Independent array of Variables",X15)
    print("<br>")
    print("<br>")
    print("Dependent array of Variables",y15)
    print("<br>")
    print("<br>")

    # Splitting the dataset into the Training set and Test set
    from sklearn.cross_validation import train_test_split
    X15_train, X15_test, y15_train, y15_test = train_test_split(X15, y15, test_size = 0.2, random_state = 0)

    print("Independent Training set: ",X15_train)
    print("<br>")
    print("<br>")
    print("Independent Testing set: ",X15_test)
    print("<br>")
    print("<br>")
    print("Dependent Training set: ",y15_train)
    print("<br>")
    print("<br>")
    print("Dependent Testing set: ",y15_test)
    print("<br>")
    print("<br>")

    print("Training set length: ",len(X15_train))
    print("<br>")
    print("<br>")
    print("Testing set length: ",len(X15_test))
    print("<br>")
    print("<br>")

    #Fit multiple linear regresion to the data
    from sklearn.linear_model import LinearRegression
    regressor15 = LinearRegression()

    regressor15.fit(X15_train,y15_train)

    #Predicting the test result
    y15_pred = regressor15.predict(X15_test)
    print("Predicted array of attributes",y15_pred)
    print("<br>")
    print("<br>")

    for index in range(len(y15_pred)):
        iter=index+1
        print ("Predictions #",iter,":", y15_pred[index], "\tActual #",iter,":",y15_test[index])
        print("<br>")
        print("<br>")
    return 0

   
"""for index in range(len(y17_pred)):
    iter=index+1
    print ("Predictions 15 #",iter,":", y15_pred[index], "\tPredictions 16 #",iter,":", y16_pred[index],"\tPredictions 17 #",iter,":", y17_pred[index])
"""


