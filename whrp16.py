# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 00:55:49 2018

@author: Shreshto
"""

def run():  
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    
    
    """#For online import
    import io
    import requests
    url16="https://raw.githubusercontent.com/Yasin-Rahman/CSV/master/2016.csv"
    s16=requests.get(url16).content
    dataset16=pd.read_csv(io.StringIO(s16.decode('utf-8')))
    #dataset16 = pd.read_csv(url16)
    """
    
    # Importing the dataset
    dataset16 = pd.read_csv('2016.csv')
    
    print("The Dataset for 2016: ",dataset16)
    
    print("Dataset Length for 2016:",len(dataset16))
    
    X16 = dataset16.iloc[:, :-1].values
    y16 = dataset16.iloc[:, 8].values
    
    print("Independent array of Variables",X16)
    print("Dependent array of Variables",y16)
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.cross_validation import train_test_split
    
    X16_train, X16_test, y16_train, y16_test = train_test_split(X16, y16, test_size = 0.2, random_state = 0)
    
    print("Independent Training set: ",X16_train)
    print("Independent Testing set: ",X16_test)
    print("Dependent Training set: ",y16_train)
    print("Dependent Testing set: ",y16_test)
    
    print("Training set length: ",len(X16_train))
    print("Testing set length: ",len(X16_test))
    
    #Fit multiple linear regresion to the data
    from sklearn.linear_model import LinearRegression
    
    regressor16 = LinearRegression()
    
    regressor16.fit(X16_train,y16_train)
    
    #Predicting the test result
    y16_pred = regressor16.predict(X16_test)
    print("Predicted array of attributes",y16_pred)
    
    for index in range(len(y16_pred)):
       iter=index+1
       print ("Predictions #",iter,":", y16_pred[index], "\tActual #",iter,":",y16_test[index])
    return 0   
    
       
"""for index in range(len(y17_pred)):
   iter=index+1
   print ("Predictions 15 #",iter,":", y15_pred[index], "\tPredictions 16 #",iter,":", y16_pred[index],"\tPredictions 17 #",iter,":", y17_pred[index])
"""
    
    
