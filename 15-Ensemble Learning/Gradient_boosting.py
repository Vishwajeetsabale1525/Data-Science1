# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:03:52 2024

@author: Vishwajeet
"""


import pandas as pd 
df=pd.read_csv("C:/Data Science/datasets/movies_classification.csv")

#Data info
df.head()
df.info()

#Dummy Variables
df=pd.get_dummies(df,columns=["3D_available","Genre"],drop_first=True)

df.head()
#input and output split
predictors=df.loc[:,df.columns!="Start_Tech_Oscar"]
type(predictors)

target=df["Start_Tech_Oscar"]
type(target)

#Train test 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(predictors,target,test_size=0.2,random_state=0)

from sklearn.ensemble import GradientBoostingClassifier

boost_clf=GradientBoostingClassifier()
boost_clf.fit(x_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix
confusion_matrix(y_test,boost_clf.predict(x_test))
accuracy_score(y_test, boost_clf.predict(x_test))

#Hyperparameters
boost_clf2=GradientBoostingClassifier(learning_rate=0.02,n_estimators=1000,max_depth=1)
boost_clf2.fit(x_train,y_train)

#Evaluation on testing data
from sklearn.metrics import accuracy_score,confusion_matrix
confusion_matrix(y_test,boost_clf2.predict(x_test))
accuracy_score(y_test, boost_clf2.predict(x_test))

