# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:04:04 2023

@author: Vishwajeet
"""




#############################################
import pandas as pd
import numpy as np
df=pd.read_csv('crime_data.csv')
#all rowss
df.shape
#multiplication of rows and col
df.size
#name of col
df.columns
#same use col....name of col
df.columns.values
df['Murder']#print the specific col
df[['Murder','Rape']]
#to show the index start and end and step
df.index
#[:] to print all rows
df3=df.loc[:,['Rape','Murder']]
df.loc[:4]    #print 0 to 4 rows
df.iloc[[2,4,6]]   #print specific rows
df['Assault'][[3,5,6]]   
df.columns=['A','B','C','D','E']
df2=df.rename(columns={'A':'c1','B':'c2'})
df3=df.drop([df.index[1]])  #drop ithe row index[1]
df3
df3=df.drop(df.index[[2,3]])  #drop the index 2 and 3
#delete index to ranfge
df3=df.drop(df.index[2:])#including 2 all rows will be deleted
df3=df.drop(df.index[2:5])#2,3,4 will be deleted
df3=df.drop(0)
df3=df.drop([1,2])
#deleted range of rows
df3=df.drop(range(0,3))
#drop specific column
df3=df.drop(["Murder"],axis=1)
df2=df.drop(labels=["Murder"],axis=1)
#############################################################
#drop col by using index
import pandas as pd
import numpy as np
df=pd.read_csv('crime_data.csv')
df2=df.drop(df.columns[1],axis=1,inplace=True)
print(df2)
df3=df.drop(df.columns[[1,3]],axis=1)
#drop column by using names
list=["Murder","Rape"]
df3=df.drop(list,axis=1)
###########################################################
import pandas as pd
import numpy as np
df=pd.read_csv('crime_data.csv')
df1=df.iloc[:]
df1=df.iloc[:,2:5]
df1=df.iloc[1:23,1:3]

df1=df.iloc[-3:]  #print last 3 rows
df1=df.iloc[:3]   #print 1st 3 rows
df1=df.iloc[::2]   #print alternate rows
df1=df.iloc[1:5]  #print rows for 1 to 4
#######################################################
df2=df.loc[:,["Murder","Rape"]]
df2=df.loc[:,'Murder']