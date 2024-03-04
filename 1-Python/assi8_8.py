# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 16:01:22 2023

@author: Vishwajeet
"""



import pandas as pd
import numpy as np
df=pd.read_csv('seeds_data.csv')
df
"""row count"""
row_count=len(df.index)
row_count                   #210
#or
row_count=len(df.axes[0])
row_count 
#or
row_count=df.shape[0]
row_count 

""" column count"""
col_count=len(df.columns)
col_count                   #8
#or
col_count=len(df.axes[1])
col_count                   #8
col_count=df.shape[1]
col_count
""" """
df.info
df.describe
""" to check any value is null in column"""
df2=(df[df['length'].isnull()])


""" to select rows whose Assymetry_coeff 
 is between 1 to 3"""

print(df[df['Assymetry_coeff'].between(2,3)])


""" to select row having width <3 and assymetry >3"""

print(df[(df['Assymetry_coeff']>3) & (df['Width']<3)])

"""to change the value of index 3 area """
df.loc[3,'Area']=14
df

""" to find mean of area"""

print(df['Area'].mean())

""" to arrange in order"""
df3=df.sort_values(by=['Area'],ascending=[False])
df3

""" to replace values """
df['qualify']=df['Type'].map({'1':True,'0':False})
df

""" """
df.columns

df.columns.values

df.dtypes

df['Area']

df[['Area','Type']]

df2=df[:2]

print(df2)

df['Area'][3]


df['Area']=df['Area']-1

df['Area']

df['Area'][3]


#delete row for position index
df1=df.drop(df.index[1])
df1

df1=df.drop(df.index[1,3])#not run
df1

#delete rows by index range
df1=df.drop(df.index[1:])
df1

#when you have default index
df1=df.drop(1)
df1
df1=df.drop([1,2])
df1


#it will drop row no. 1 and 2
df1=df.drop(range(0,2))
df1

#it will delete rows in range 0 to 2
############################################################################################
df.drop(df.columns[1],axis=1,inplace=True)
print(df)
df=pd.read_csv("seeds_data.csv")


#drop 2 or more columns by index
df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)
###################################################


#drop columns from list of columns
df.columns
lisCol=["Area","Type"]
df2=df.drop(lisCol,axis=1)
print(df2)

df2=df.iloc[[0,2,4]]#select row 0,2,4
df2
df2=df.iloc[1:5]    #select row in range 1 to 5 (excluding 5)
df2
df2=df.iloc[:1]     #select first row
df2
df2=df.iloc[-1:]    #select last row
df2
df2=df.iloc[-3:]    #select last 3 rows
df2
df2=df.iloc[::2]  #select alternate rows
df2

df2=df.loc[:,["Area","Type"]]
df2

#slect multiple columns
df2=df.loc[:,["Area","Type"]]
df2


#select columns between tow columns
df2=df.loc[:,"Area","Type"] #not run
""""IndexingError: Too many indexers"""
df2


#slect column by range
df2=df.loc[:,:'Area']
df2