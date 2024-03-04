# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 09:30:51 2024

@author: Vishwajeet
"""

import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import warnings
warnings.filterwarnings('ignore')
#Read csv file
loan_data=pd.read_csv("C:/Data Science/datasets/income.csv")
loan_data.columns
loan_data.head()
#Let us split the data in input and output
x=loan_data.iloc[:,0:6]
y=loan_data.iloc[:,6]
#Split the dataset
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
#Create Adaboost Classifier
ada_model=AdaBoostClassifier(n_estimators=100,learning_rate=1)
#n_estimetors=number of weak learner
#Learining rate it contributes weights of waek learners,by default it is
#train the model
model=ada_model.fit(x_train,y_train)
#Predict the result
y_pred=model.predict(x_test)
print("Accusracy",metrics.accuracy_score(y_test, y_pred))
#Let us try for another base model
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
#Here base model is changed
ada_model=AdaBoostClassifier(n_estimators=50,base_estimator=lr,)
model=ada_model.fit(x_train,y_train)

y_pred=model.predict(x_test)
print("Accuracy",metrics.accuracy_score(y_test, y_pred))