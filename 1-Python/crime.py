# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:53:57 2023

@author: Vishwajeet
"""

import pandas as pd
import numpy as np
df=pd.read_csv('loan.csv')
df.shape
print(df)
df.size
df.columns
df.columns.values
df.index
#accessing single col values
df['member_id']
#accesing two col values
df[['term','member_id']]
#select certain rows and assign a dataframes
df2=df.loc[:,["id","member_id"]]
df2=df.iloc[[2,5,7]]
df['term'][3]
#substracting specific col values
df3=df['loan_amnt']=df['loan_amnt']-1000
print(df3)

d5=df.describe()
print(d5)
#delete rowa index
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,8]])
df1
#range
df1=df.drop(df.index[6:])
df1=df.drop(range(1,8))   #it will be deleted 1 to 7 drop
df2=df.iloc[:,0:8]
df2=df.iloc[1:4,1:5]
df2=df.iloc[:3]
df2=df.iloc[4:]
df2=df.iloc[-5:]
df2=df.iloc[::3]
df2=df.loc[:,["term","id"]]
#sselect col between two col
df2=df.loc[:,'member_id':'term']
print(df2)
#select col by range
df2=df.loc[329:334,'id']