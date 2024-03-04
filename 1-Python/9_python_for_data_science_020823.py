#--------------------DATE ===>02/08/2023-------------------------#
##################################################################
#------------------PYTHON FOR DATA SCIENCE------------------------
##################################################################    

'''
A series is used to model one dimensional data, similar to a list in 
 python .  The series object also have a few more bits of data, including
  an #index and name.
'''

import pandas as pd
songs2=pd.Series([145,142,38,13],name='counts')
#It is easy to inspect the index of a series
songs2.index #Here we can find the index
songs2
#The index can string base as well
#in which case pandas indicates
#that the datatype for the index is object
song3=pd.Series([145,142,38,13],name='counts',index=['Om','Sai','Ram','Prajwal'])
song3.index
song3
#the NuN value
#This value stands for Not A number, and is usally ignored 
#in arithmatik oprations.
#(similer to NULL in SQL).
#If you load data from CSV file,
#an empty value for an otherwise

#numeric coloum will become NaN.
#what is real and absolute 

import pandas as pd
f1=pd.read_csv('c:/1-python/age.csv')
f1


import pandas as pd
f2=pd.read_excel('c:/1-python/Bahaman.xlsx')
f2

#############################################################
#for numpy---->pip install numpy
import numpy as np
numpy_ser = np.array([145,142,38,13])
song3[1]  #accesing series element
#142.
numpy_ser[1]
numpy_ser.mean()

############################################################

#the PANDAS SERIES DATA STRUCTURE PROVIDES SOPPORT FOR THE BASIC CRUD
#Operations-create,read, update and delete
#creation
george=pd.Series([10,7,1,22])
index = ['1968','1969','1970','1970']
name ='George Songs'
george


'''
The privious example illustrates an intresting feature of pandas
the index values are strings and they are not unique .This can 
couse some confusion, but can also be useful when duplicate 
items are neded 
'''
#Reading 
#To read or select the data from a series

george['1968']

george['1970']
#we can iterate over data in series as well
#when iterating over a series
for item in george:
    print(item)

##########################################################
#Updating
#Updating values in a series can be little tricky as well.
#to update a value
#for a given index lable
#the standerd index assignment opration, 
#work

george['1969'] = 68
george['1969']

#########################################
#Deletion
#The del statement appears to have 
#problems with duplicate index

s = pd.Series([2,3,4],index=[1,2,3])
del s[1]
s

#################################################################

#convert type
#string use.astype(str)
#numeric use pd.to_numeric
#integer use .astype(int)
#note that this will fail with NaN
#datetime use pd.to_datetime

songs_66 = pd.Series([3, None, 11, 9], index=['George','Ringo','John','Paul'],name='Counts')
songs_66.dtypes
#dtype('float64')
pd.to_numeric(songs_66.apply(str))
#There will be error
pd.to_numeric(songs_66.astype(str),errors='coerce')
#if we pass errors='coerce',
#we can see that it supports many formats
songs_66.dtypes

#dealing with None 
#the .fillna method will replace them with a given value
songs_66.fillna(-1)

#NaN values can be dropped from 
#the series using .dropma
songs_66.dropna()

###########################################################
#Append,combining, and joining two series
songs_69 = pd.Series([7,16,21,39],
index=['Ram','Sham','Ghansham,','Krishna'],name='Counts')
#To concatenate two series together,simply use the .append
songs=songs_66.append(songs_69)

##########################################################
#Installing matplotlib
#pip install matplotlib

#Plotting series
import matplotlib.pyplot as plt
fig = plt.figure()
songs_69.plot()
plt.legend()

########################################################
#bar graph
fig = plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()

###################################################
#Hisogram
import numpy as np
data = pd.Series(np.random.randn(500),name='500 random')
fig = plt.figure()
ax = fig.add_subplot(111)
data.hist()

###############################################################

#What is pandas DataFrame?

#upgreade comand conda
#conda install --upgrade pandas
#conda install -c anaconda pandas

#letest version 2.0.3

#To check the version of pandas
import pandas as pd
pd.__version__

#create using constructor
#create pandas Dataframe from list
import pandas as pd
technologies = [["Spark",20000, "30days"],["Pandas",20000,"40days"]]
df=pd.DataFrame(technologies)
print(df)

#Since we have not given coloums and 
#indexes, DataFrame by defualt assigns
#incremental sequence numbers as lebel 
#to both rows and coloums, these are called Index.
#Add coloum and Row labels to the DataFrame
column_names = ["Courses",'Fees','Duration']
row_labels = ["a","b"]
df = pd.DataFrame(technologies,columns=column_names,index=row_labels)
print(df)

####################################################
df.dtypes
#################
#you can also assign custom
#data type to coloumn
##set custom types to DataFrame

#DataFrame ----->1)coloumn and 2)Rows
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fee': [20000,25000,26000,22000,24000,21000,22000],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df = pd.DataFrame(technologies)
print(df.dtypes)

#convert all types to best possible types
df2=df.convert_dtypes()
print(df2.dtypes)
#change all coloums to same type
df = df.astype(str)
print(df.dtypes)

#Change type for one or multiple coloums (imp)
df = df.astype({"Fee": int, "Discount": float})
print(df.dtypes)

#Convert Data Type for all coloumns in a list
df = pd.DataFrame(technologies)
df.dtypes
cols = ['Fee','Discount']
df[cols] = df[cols].astype('float')
df.dtypes
#Ignores error
df = df.astype({"Courses":int},errors='ignore')
df.dtypes
#Genrate error
df = df.astype({"Courses":int},errors='raise')
#Convert feed coloum to numeric type
df = df.astype(str)






















