# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 21:01:41 2023

@author: Vishwajeet
"""

import pandas as pd
import numpy as np
df=pd.read_csv('bank_data.csv')
df.shape    #rows and col
df.size     #multiplication of rows and col
df.columns  #show the name of col
df.columns.values  #show the name of col
df.index
df.describe
df.info   #rows and col[45211 rows x 32 columns]
df.iloc[2]
'''
age                33
default             0
balance             2
housing             1
loan                1
duration           76
campaign            1
pdays              -1
previous            0
poutfailure         0
poutother           0
poutsuccess         0
poutunknown         1
con_cellular        0
con_telephone       0
con_unknown         1
divorced            0
married             1
single              0
joadmin.            0
joblue.collar       0
joentrepreneur      1
johousemaid         0
jomanagement        0
joretired           0
joself.employed     0
joservices          0
jostudent           0
jotechnician        0
jounemployed        0
jounknown           0
y                   0
Name: 2, dtype: int64
'''
df2=df.iloc[[2,4,6]]     #aaceesing data for multiple rows
######################################################################
#accesing data for one col contents
df["age"]
#accesing data for multiple column
df[["age","balance"]]
#accessing range of data
df2=df[2:12]
df2=df[:4]
#accessing certain celll
df["age"][3]
#substracting values from columns
df['duration']=df['duration']-100
#delete rows or index
df3=df.drop(df.index[1])
#delee multiple index
df3=df.drop(df.index[[5,2,3]])
#delete index range
df3=df.drop(range(0,6))
df3=df.drop(df.index[:4])
#0th rows will be delete
df3=df.drop(0)
############################################################
#specific rows will be deleted without using index
df.drop([2])
df3=df.drop([2,4,5])
#deleted range of rows
df3=df.drop(range(4,9))
############################################################
#deleted specific column
df3=df.drop(["duration"],axis=1)
df3=df.drop(["age",'duration'],axis=1)

#############################################################
###########################################################
#############################################################
#drop col using index
df3=df.drop(df.columns[[1,3]],axis=1)
df3=df.drop(df.columns[2],axis=1,inplace=True)
#deleting multiple column
df3=df.drop(df.columns[[3,4,1]],axis=1)
listcol=["age","duration"]
df3=df.drop(listcol,axis=1)

##############################################################
###############################################################
##############iloc************************************8
df3=df.iloc[:]
df3=df.iloc[:,1:3]
df3=df.iloc[1:5,1:3]
df3=df.iloc[1:5,:]
#############################################################
#############################################################
#selecting rowsby integer values
df3=df.iloc[[2,3,4]]
df3=df.iloc[:-3]   #excluding last 3 rows all rows will be printed
df3=df.iloc[-3:]   #last three rows printes
df3=df.iloc[:3]
df3=df.iloc[3:]
######################################################################
######################################################################
#selecting multiple columns
df3=df.loc[:,["age","duration"]]
#for selecting specific column range
df3=df.loc[:,"loan":"pdays"]


