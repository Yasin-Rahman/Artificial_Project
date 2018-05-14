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
    url17="https://raw.githubusercontent.com/Yasin-Rahman/CSV/master/2017.csv"
    s17=requests.get(url17).content
    dataset17=pd.read_csv(io.StringIO(s17.decode('utf-8')))
    #dataset17 = pd.read_csv(url17)"""
    
    # Importing the dataset
    
    dataset17 = pd.read_csv('2017.csv')
    
    print("The Dataset for 2017: ",dataset17)
    
    print("Dataset Length for 2017:",len(dataset17))
    
    
    X17 = dataset17.iloc[:, :-1].values
    y17 = dataset17.iloc[:, 8].values
    
    
    
    print("Independent array of Variables",X17)
    print("Dependent array of Variables",y17)
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.cross_validation import train_test_split
    
    X17_train, X17_test, y17_train, y17_test = train_test_split(X17, y17, test_size = 0.2, random_state = 0)
    
    print("Independent Training set: ",X17_train)
    print("Independent Testing set: ",X17_test)
    print("Dependent Training set: ",y17_train)
    print("Dependent Testing set: ",y17_test)
    
    print("Training set length: ",len(X17_train))
    print("Testing set length: ",len(X17_test))
    
    #Fit multiple linear regresion to the data
    from sklearn.linear_model import LinearRegression
    
    regressor17 = LinearRegression()
    
    regressor17.fit(X17_train,y17_train)
    
    #Predicting the test result
    y17_pred = regressor17.predict(X17_test)
    print("Predicted array of attributes",y17_pred)
    
    for index in range(len(y17_pred)):
       iter=index+1
       print ("Predictions #",iter,":", y17_pred[index], "\tActual #",iter,":",y17_test[index])
    return 0
        
"""for index in range(len(y17_pred)):
   iter=index+1
   print ("Predictions 15 #",iter,":", y15_pred[index], "\tPredictions 16 #",iter,":", y16_pred[index],"\tPredictions 17 #",iter,":", y17_pred[index])
"""
    
    
