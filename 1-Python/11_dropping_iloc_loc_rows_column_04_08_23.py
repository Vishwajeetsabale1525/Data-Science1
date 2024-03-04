
#---------------------------------------------#
##################################################################
#---------------DATE ===>04/08/2023-----Friday-------------------
##################################################################    

import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fee':[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days','60days','50days','55days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
row_labels = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies)
print(df.dtypes)
#Drop DataFrame Rows and columns
df = pd.DataFrame(technologies,index=row_labels)

#drop rows by lables
#(single sqaure bracket)

#Drop rows by lables
df1=df.drop(['r1','r2'])
df1

#Delete rows by index range 
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,3]])
df1

#Delete ros by index column 
df1 = df.drop(df.index[2:])
df1

#When you have default indexes for rows 
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1
df=pd.Dataframe(technologies)
df1=df.drop([0,3])          #it will delete row0 n row3
df1=df.drop(range(0,2))     #it will delete 0 and 1

# Droping of Columns ==>
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java","SQL"],
    'Fee':[20000,25000,26000,22000,np.nan,21000,22000,25000],
    'Duration':['30days','40days','35days','50days','60days','','55days','35days']}
df = pd.DataFrame(technologies)
print(df)

#1) Drop column by name
#Drop fee column

df2 = df.drop(["Fee"],axis=1)
print(df2)

#Explicitly using parameter name 'labels'
df2=df.drop(labels=["Fee"], axis=1)

#Alternatively you can also use column instead of lebels
df2=df.drop(columns = ["Fee"],axis=1)

#Drop column by index
print(df.drop(df.columns[1],axis=1))

df = pd.DataFrame(technologies)

#using inplace=True
df.drop(df.columns[2], axis=1, inplace=True)
print(df)

##############################################
df = pd.DataFrame(technologies)
#Drop two or more columns By label name
df2=df.drop(["Courses","Fee"], axis=1)
print(df2)

#Drop two or more columns By index
df = pd.DataFrame(technologies)

df2 =df.drop(df.columns[[0,1]], axis = 1)
print(df2)
###################################
#Drop columns from list of columns
df = pd.DataFrame(technologies)
df.columns
lisCol=["Courses","Fee"]
df2=df.drop(lisCol, axis=1)
print(df2)

#################################################################

#################################################################

#pandas select Rows by index use of iloc

import pandas as pd
import numpy as np # --> but not needed here 
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","None","Spark","Python"],
    'Fee':[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30days','50days','55days','40days','60days','35days','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
    }
row_labels = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies)
print(df)

#  iloc --> Syntax
# df.iloc[startrow:endrow , startcolm:endcolm]

df = pd.DataFrame(technologies,index=row_labels)
#Below are quick example
df2 = df.iloc[:,0:2]
df2

#This line uses the slicing operation to get DataFrame items by index
#The first slice [:] indicates to return all rows
#The secomd slice specifies that only columns
#between 0 and 2 (excluding 2) should be return

df2=df.iloc[0:2, :]
df2
#in this case the first slice[0:2] is
#requesting only rows 0 throught 1 of the DataFrame
#The second slice[:] indicates that all columns

#Slicing specific rows and columns using iloc and 
df3 = df.iloc[1:2,1:3]
df3

#the second oprator [1:3] yields columns 1 and Select rows by integer index
df2 = df.iloc[2]  #select rows by index
df2

df2 = df.iloc[[2,3,6]] #Select Rows by index list
df2 = df.iloc[1:5]     #Select Rows by integer index range
df2 = df.iloc[:1]      #Select First row
df2 = df.iloc[:3]      #Select first 3 rows
df2 = df.iloc[-1:]     #Select last row
df2 = df.iloc[-3:]     #Select last 3 row
df2 = df.iloc[::2]     #Select alternate rows 

####################################################

#Select rows by index using loc

df2 = df.loc['r2'] #select row by label
df2 = df.loc[['r2','r3','r6']] #select rows by index
df2 = df.loc['r1':'r5'] #select rows by label index
df2 = df.loc['r1':'r5':2] #


#Using loc[] to take columns slice
#loc[] syntax to slice column
 #typing remaining photo
 
#Using loc[] to take column slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]

##Select multiple columns 
df2 = df.loc[:,["Courses","Fee","Duration"]]

#Select Random Columns
df2 = df.loc[:,["Courses","Fee","Discount"]]

#Select Columns between two columns
df2 = df.loc[:,"Fee":"Discount"]

#Select Columns by range
df2 = df.loc[:,"Duration":]

#Select Columns by range
# All the columns upto 'Duration'
df2 = df.loc[:,:"Duration"]
