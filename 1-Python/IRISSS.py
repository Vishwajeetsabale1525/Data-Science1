# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 16:07:12 2023

@author: Vishwajeet
"""

import pandas as pd
df=pd.read_csv('Iris.csv')
df
df.shape    #col nd rows
df.size     #col*row
df.columns
#or21
df.columns.values  #col names
df.index
df.info
res=df.iloc[[2,3,4,6]]  #give the index of 2,3,4,6
#Accessing one col values
df['Species']
#Accessing two col values
df["Species"]
#select a certain rows and assign a certain dataframes
df3=df[:4] #return 0 to 3
df3=df[4:] #return all rows with 4
###########################################################3
#accesing data from specific col
df4=df['Species'][6]
################substracting data from specific col
df['PetalLengthCm']=df['PetalLengthCm']-0.1
df.describe()
##########################################
#drop the row by index
df3=df.drop(df.index[1])
#drop the multiple index
df3=df.drop(df.index[[4,6]])
#drop the rows by range
df3=df.drop(range(2,6))
df3=df.drop(0)
#delete specific row 1 nd 3
df3=df.drop(["Species"],axis=1)
#using inplace =true
df2=df.drop(df.columns[2],axis=1,inplace=True)
#########################################################3
#deleting multiple columns
df2=df.drop(df.columns[[3,1]],axis=1)
#drop list of col
listcol=["PetalLengthCm","PetalWidthCm"]
df3=df.drop(listcol,axis=1)
###########################################3
#iloc
df3=df.iloc[:]
df3=df.iloc[:3]  #return 0,1,2
df3=df.iloc[3:]  #except 0,1,2 all rows are return
df3=df.iloc[0:8]# 0 to 7 will be return
df3=df.iloc[:,4:8]
df3=df.iloc[1:10,1:3]
df3=df.iloc[3]
df3=df.iloc[[2,3,4]]
df3=df.iloc[2:6]
df3=df.iloc[-3]  #return last third row
df3=df.iloc[3]
df3=df.iloc[:-3]  #except last 3 all rows are return
df3=df.iloc[:3]   #return only first 3 rows
df3=df.iloc[-3:]  #only last 3 records will be return
df3=df.iloc[3:]   #except 0,1,2 all rows will be return
df3=df.iloc[::2]  #alternate rows will be retuen like 0,2,4...

####################################################
#select col between 2 columns
df3=df.loc[:,"SepalLengthCm":"Species"]
df3=df.loc[:,["Species","SepalLengthCm"]]
df3=df.loc[:,"Species"]
df3=df.loc[4:9,"Species"]
###################################################3
df2=df.query("Species=='Iris-setosa'")
print(df2)
###Not equals 
df2=df.query("Species!='Iris-setosa'")
print(df2)


###################################################
#add new col to dataframes
#price=[200,344,900,256,789,900,678,453,567]
#df2=df.assign(PriceAssigned=price)
#################################################
rows_count=len(df.index)#rows count
rows_count
col_count=len(df.axes[1])
col_count  #col count
rows_count=len(df.axes[0])
rows_count

row_count=df.shape[0]  #total no of rows
row_count=df.shape[1]  #total no of columns
##################################################
#check the null value in the col
df2=(df[df['Species'].isnull()])

print(df[df['SepalLengthCm'].between(2,3)])

#to change the value of index 4
df.loc[4,'SepalLengthCm']=6
#to arrange data in some order
df3=df.sort_values(by=['SepalLengthCm'],ascending=[False])
df3
#shuffle rows
df1=df.sample(frac=1)
print(df1)
#create new index
df1=df.sample(frac=1).reset_index()
print(df1)
#group by
df2=df.groupby(['Species']).sum()
df2
#group by multiple col
df2=df.groupby([['Species','SepalLengthCm']]).sum()
df2




