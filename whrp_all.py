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
    url16="https://raw.githubusercontent.com/Yasin-Rahman/CSV/master/2016.csv"
    url17="https://raw.githubusercontent.com/Yasin-Rahman/CSV/master/2017.csv"
    s15=requests.get(url15).content
    s16=requests.get(url16).content
    s17=requests.get(url17).content
    dataset15=pd.read_csv(io.StringIO(s15.decode('utf-8')))
    dataset16=pd.read_csv(io.StringIO(s16.decode('utf-8')))
    dataset17=pd.read_csv(io.StringIO(s17.decode('utf-8')))
    #dataset15 = pd.read_csv(url15)
    #dataset16 = pd.read_csv(url16)
    #dataset17 = pd.read_csv(url17)"""
    
    # Importing the dataset
    dataset15 = pd.read_csv('2015.csv')
    dataset16 = pd.read_csv('2016.csv')
    dataset17 = pd.read_csv('2017.csv')
    
    print("The Dataset for 2015: ",dataset15)
    print("The Dataset for 2016: ",dataset16)
    print("The Dataset for 2017: ",dataset17)
    
    print("Dataset Length for 2015:",len(dataset15))
    print("Dataset Length for 2016:",len(dataset16))
    print("Dataset Length for 2017:",len(dataset17))
    
    X15 = dataset15.iloc[:, :-1].values
    y15 = dataset15.iloc[:, 8].values
    X16 = dataset16.iloc[:, :-1].values
    y16 = dataset16.iloc[:, 8].values
    X17 = dataset17.iloc[:, :-1].values
    y17 = dataset17.iloc[:, 8].values
    
    print("Independent array of Variables(15)",X15)
    print("Dependent array of Variables(15)",y15)
    
    print("Independent array of Variables(16)",X16)
    print("Dependent array of Variables(16)",y16)
    
    print("Independent array of Variables(17)",X17)
    print("Dependent array of Variables(17)",y17)
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.cross_validation import train_test_split
    X15_train, X15_test, y15_train, y15_test = train_test_split(X15, y15, test_size = 0.2, random_state = 0)
    X16_train, X16_test, y16_train, y16_test = train_test_split(X16, y16, test_size = 0.2, random_state = 0)
    X17_train, X17_test, y17_train, y17_test = train_test_split(X17, y17, test_size = 0.2, random_state = 0)
    
    print("Independent Training set(15): ",X15_train)
    print("Independent Testing set(15): ",X15_test)
    print("Dependent Training set(15): ",y15_train)
    print("Dependent Testing set(15): ",y15_test)
    
    print("Independent Training set(16): ",X16_train)
    print("Independent Testing set(16): ",X16_test)
    print("Dependent Training set(16): ",y16_train)
    print("Dependent Testing set(16): ",y16_test)
    
    print("Independent Training set(17): ",X17_train)
    print("Independent Testing set(17): ",X17_test)
    print("Dependent Training set(17): ",y17_train)
    print("Dependent Testing set(17): ",y17_test)
    
    print("Training set length(15): ",len(X15_train))
    print("Testing set length(15): ",len(X15_test))
    
    print("Training set length(16): ",len(X16_train))
    print("Testing set length(16): ",len(X16_test))
    
    print("Training set length(17): ",len(X17_train))
    print("Testing set length(17): ",len(X17_test))
    
    
    #Fit multiple linear regresion to the data
    from sklearn.linear_model import LinearRegression
    regressor15 = LinearRegression()
    regressor16 = LinearRegression()
    regressor17 = LinearRegression()
    
    regressor15.fit(X15_train,y15_train)
    
    regressor16.fit(X16_train,y16_train)
    
    regressor17.fit(X17_train,y17_train)
    
    #Predicting the test result
    y15_pred = regressor15.predict(X15_test)
    print("Predicted array of attributes(15):",y15_pred)
    
    y16_pred = regressor16.predict(X16_test)
    print("Predicted array of attributes(16):",y16_pred)
    
    y17_pred = regressor17.predict(X17_test)
    print("Predicted array of attributes(17):",y17_pred)
    
    for index in range(len(y15_pred)):
       iter=index+1
       print ("Predictions(2015) #",iter,":", y15_pred[index], "\tActual(2015) #",iter,":",y15_test[index])
    print("2015 Done!\n")
       
    for index in range(len(y16_pred)):
       iter=index+1
       print ("Predictions(2016) #",iter,":", y16_pred[index], "\tActual(2016) #",iter,":",y16_test[index])
    print("2016 Done!\n")
       
    for index in range(len(y17_pred)):
       iter=index+1
       print ("Predictions(2017) #",iter,":", y17_pred[index], "\tActual(2017) #",iter,":",y17_test[index])
    print("2017 Done!\n")
    
    
    
