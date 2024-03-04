# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:24:23 2023

@author: Vishwajeet
"""
# DATAFRAMES IN PYTHON
 #   -upgrade pandas- on base terminal(anaconda navigator), 
'''  "conda install --upgrade pandas"
    or
    "Conda install -C anaconda pandas"
    -To upgrade to specific version
    "conda install pandas==2.0.3"
    '''
#To know which version of pandas
import pandas as pd
pd._version_  #its underscore underscore
    
##############################################################

#               Creating Dataframes
#Using the Constructor
#Create pandas dataframe from the list
import pandas as pd
technologies=[["spark",1000,"30days"],
              ["pandas",2000,"40days"]]    
df=pd.DataFrame(technologies) 
print(df)   
'''
Output-
        0     1       2
0   spark  1000  30days
1  pandas  2000  40days   
'''
#Since we did not assign any labels to rows and columns
#   it takes up default incremental values as labels to both
#    rows and columns, these are called Index

#*********************

#Adding rows and columns labels to dataframes(Index)

column_name=["Courses","Fees","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_name,index=row_label)
print(df)
 
#*********************

#Datatypes of The Dataframe
df.dtypes    

#*********************

#Now, we can column_names(namings) the DataFrame inbuilt
#We use dictionaries    

technologies={
    'Courses':["Spark","Hadoop","PSpark","Python","Pandas","Oracle"],
    'Fees':[2000,5000,2500,7000,6700,2800],
    'Duration':["30days","40days","70days","45days","90days","15days"],
    'Discount':[11.8,33.9,42.9,27.9,36.8,77.2]
    } #Each category must have equal number of entities and 
        # Commas are important!
df=pd.DataFrame(technologies)
print(df)
print(df.dtypes)
'''     Output
 Courses  Fees Duration  Discount
0   Spark  2000   30days      11.8
1  Hadoop  5000   40days      33.9
2  PSpark  2500   70days      42.9
3  Python  7000   45days      27.9
4  Pandas  6700   90days      36.8
5  Oracle  2800   15days      77.2
Courses      object
Fees          int64
Duration     object
Discount    float64
dtype: object
'''
#-----------------------------------------------------------
#Important
#Converting all datatypes to the best possible types
df2=df.convert_dtypes()
print(df2.dtypes) #Converts 'object' to 'string'
#-----------------------------------------------------------
#Change all the columns to same type
df=df.astype(str)
print(df.dtypes)    #Converting every datatype to 'object'
#-----------------------------------------------------------
#Changing datatype for one or many columns
#Commonly used
df=df.astype({"Fees":int,"Discount":float}) #Passed as dictionaries
print(df.dtypes)
#-----------------------------------------------------------
#Converting datatypes for one or multiple columns
df=pd.DataFrame(technologies)
df.dtypes

cols=['Fees','Discount']
df[cols]=df[cols].astype('float')
df.dtypes
#********************
#                   Ignoring errors
df=df.astype({"Courses":int},errors='ignore')
df.dtypes  #Not going to change the datatype
#-----------------------------------------------------------
#                   Creating the error
df=df.astype({"Courses":int},errors='raise')
df.dtypes   #Raises error

#*********************

technologies={
    'Courses':["Spark","Hadoop","PSpark","Python","Pandas","Oracle"],
    'Fees':[2000,5000,2500,7000,6700,2800],
    'Duration':["30days","40days","70days","45days","90days","15days"],
    'Discount':[11.8,33.9,42.9,27.9,36.8,77.2]
    } 
row_labels=['r0','r1','r2','r3','r4','r5']
df=pd.DataFrame(technologies,index=row_labels)
df=pd.DataFrame(technologies)
#convert dataframe to csv
df.to_csv('data_file.csv')
#create dataframe from csv file
df=pd.read_csv('data_file.csv')
##################################
#dataframe properties
df.shape
#(6,4)
df.size#multiplivation of row nd col
#24
df.columns
df.columns.values
df.index
df.info
res=df.iloc[[2,3,4]]
res

##########################################33
#accessing one col content
df['Fees']
#Accessing two col contents
df[['Fees','Duration']]

#select certainrows and assign to certain dataframes
df2=df[4:]
df2

##########################################
#accessing certain cell from col 'Duration'
df['Duration'][3]
#substracting specing values from col
df['Fees']=df['Fees']-500
df['Fees']
#pandas to manipulate dataframe
#Describ dataframe
#Describe dataframe to all numeric col
#function
df.describe()
'''
  Fees   Discount
count     6.000000   6.000000
mean   3333.333333  38.416667
std    2205.145498  21.754578
min    1000.000000  11.800000
25%    1575.000000  29.400000
50%    2900.000000  35.350000
75%    5275.000000  41.375000
max    6000.000000  77.200000
'''
#it will show 5 no summaryy
#############################################
#rename()-renming pandas dataframe colum names
df=pd.DataFrame(technologies,index=row_labels)
 #assigning a new header by setting new col values
df.columns=['A','B','C','D']

##############################################
#rename() col name using rename() method
df=pd.DataFrame(technologies,index=row_labels)
 #assigning a new header by setting new col values
df.columns=['A','B','C','D']
df2=df.rename({'A':'c1','B':'c2'},axis=1)
df2=df.rename({'C':'C3','D':'C4'},axis='columns')
#another way
df2=df2.rename(columns={'A':'c1','B':'c2'})
#############################################
#Drop dataframe rows and columns
#drop by label
technologies={
    'Courses':["Spark","Hadoop","PSpark","Python","Pandas","Oracle"],
    'Fees':[2000,5000,2500,7000,6700,2800],
    'Duration':["30days","40days","70days","45days","90days","15days"],
    'Discount':[11.8,33.9,42.9,27.9,36.8,77.2]
    } 
row_labels=['r0','r1','r2','r3','r4','r5']
df=pd.DataFrame(technologies,index=row_labels
                )
#drop rows by labels
df1=df.drop(['r1','r2'])
df1
#delete rowa for position/index
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,3]])
df1
#delete index to range
df1=df.drop(df.index[2:])
#when you have default index for rows
df=pd.DataFrame(technologies)
#0th rows will be deleted
df1=df.drop(0)
#specic rows deleted 1 and 2
df1=df.drop([1,2])
#deleted range of rows
df1=df.drop(range(0,3))   #it will be deleted 0,1,2
#drop spexific column
df2=df.drop(["Fees"],axis=1)
#Exiplicitlyy using parameter name label
df2=df.drop(labels=["Fees"],axis=1)


############################################
#drop column using index
technologies={
    'Courses':["Spark","Hadoop","PSpark","Python","Pandas","Oracle"],
    'Fees':[2000,5000,2500,7000,6700,2800],
    'Duration':["30days","40days","70days","45days","90days","15days"],
    'Discount':[11.8,33.9,42.9,27.9,36.8,77.2]
    } 
row_labels=['r0','r1','r2','r3','r4','r5']
df=pd.DataFrame(technologies,index=row_labels)
print(df.drop(df.columns[1],axis=1))
print(df)
#using inplace=True
df2=df.drop(df.columns[1],axis=1,inplace=True)
print(df2)
#####################################################
#drop col by index

df=pd.DataFrame(technologies)
#deletiong multiple columnn
df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)
######################################################
#Drop col from list of columns
df=pd.DataFrame(technologies)
listCol=["Courses","Fees"]
df3=df.drop(listCol,axis=1)
##################################################################

technologies={
    'Courses':["Spark","Hadoop","PSpark","Python","Pandas","Oracle"],
    'Fees':[2000,5000,2500,7000,6700,2800],
    'Duration':["30days","40days","70days","45days","90days","15days"],
    'Discount':[11.8,33.9,42.9,27.9,36.8,77.2]
    } 
row_labels=['r0','r1','r2','r3','r4','r5']
df=pd.DataFrame(technologies,index=row_labels)
print(df)

#df.iloc 
df=pd.DataFrame(technologies,index=row_labels)
df2=df.iloc[:,0:2]
df2
#this lines uses the slicing operator to get frame
#item by index
#the first slice[:]indicates to return all rows
#the second slice specifies that only col
#between 0 and 2 (exluding 2) should be returned
df2=df.iloc[0:2,:]
###############################################3
#slicing specific rows and specific col
df3=df.iloc[1:2,1:3]
df3      #1:2-excluding 2 all rows
#1:3 -excluding 3 all columns
################################################
#select rows by integer value
df2=df.iloc[2]  #select rows by index,select only one col
df2=df.iloc[[2,3,5]]   #select rows by index
df2=df.iloc[1:5]  #select rows by int index range
df2=df.iloc[:1]    #select first row
df2=df.iloc[:3]    #select first 3 row
df2=df.iloc[-1:]   #slect last row
df2=df.iloc[-3:]   #select last 3 rows
df2=df.iloc[::2]   #select alternate row
###########################################################
#select rows by index labels
df2=df.loc['r2']    #select rows by labels

df2=df.loc[['r2','r3','r4']]   #select rows by label index
df2=df.loc['r1':'r5']    #select rows by label index range
df2=df.loc['r1':'r5':2]   #select alternate rows

####################################################################
df=pd.DataFrame(technologies)
#select multiple col

df2=df.loc[:,["Courses","Fees","Duration"]]
#sselect col between two col
df2=df.loc[:,'Fees':'Discount']
print(df2)
'''
Fees Duration  Discount
0  2000   30days      11.8
1  5000   40days      33.9
2  2500   70days      42.9
3  7000   45days      27.9
4  6700   90days      36.8
5  2800   15days      77.2
'''
########################################################################


#select col by range
df2=df.loc[:,'Duration']