'''
A series is used to model one dimensional data, similar to
List in python
#The series object also has a few more bits if data including
an index and a name
'''

#                       Series
#How many times songs have been sold in that website
import pandas as pd
songs=pd.Series([145,142,38,39],name='counts')
songs.index #Inspecting index of data, which is by default number

#********************
#Index can be string based as well
#Eg
songs2=pd.Series([145,142,38,39],name='counts',index=['Paul','George','John','Rongo'])
songs2.index
songs2
###############################################################
#The NaN value(NaN=Not a Number)
#Data scientists hate NaN
#Usually ignored in arithmatic operations
#Similar to NULL in SQL
#If you load data from CSV file, an empty value for an otherwise
#       numeric value will become NaN

import pandas as pd
file=pd.read_csv("C:/1-python/age.csv")
file
#   OR
import pandas as pd
file=pd.read_csv("age.csv")
file

#Another eg
import pandas as pd
file1=pd.read_excel("C:/1-python/Bahaman.xlsx")
file1

#None, NaN, nan and null are synonyms

#############################################################
#                   NumPy
#The series object behaves like a NumPy array

import numpy as np
numpy_sr=np.array([145,142,38,39]) #numpy_sr is an array
#songs2[1]
numpy_sr[1]
numpy_sr.mean() #To find the mean

#                   Panda Series
#THE PANDA SERIES DATA STRUCTURE PROVIDES SUPPORT FOR THE BASIC CRUD
# operations- Create,Read,Update and Delete

#------------------------------------------------------------
#               Creation
george=pd.Series([10,7,1,22],index=['1968','1969','1970','1970'],name='George Songs' )
#Index can be repeated
# for different events can take place in same year
#This concept is not available in arrays and lists

george
#------------------------------------------------------------
#               Reading
#To read a data from a series
george['1968']
george['1970']

#Iterating over series
for item in george:
    print(item)
#------------------------------------------------------------
#               Updating
#Can be tricky
george['1968']=68
george['1968']
#------------------------------------------------------------
#               Deletion
s=pd.Series([11,22,33,44],index=[1,2,3,4])
del s[1] #Deleting with index
s
############################################################

#Convert Index
songs_66=pd.Series([3,None,11,9],index=['George','Paul','John','Ringo'],name='Counts')
songs_66.dtypes
#dtypes('float64')
#*********************
#Changing datatype
pd.to_numeric(songs_66.apply(str)) #Here we are changing to string datatype
#There will be an  because of NaN value(s)
pd.to_numeric(songs_66.astype(str),errors='coerce')
#Passing errors='coerce' supports many formats
#   coerce ignores NaN
songs_66.dtypes
#-----------------------------------------------------------
#Dealing None values
#We can put -1 in place of None
# With fillna(-1) method

songs_66.fillna(-1)
#-----------------------------------------------------------
#Another method to deal with None is droping the whole row
#We use dropna()

songs_66.dropna()

#This is the least recommended method as it will end up losing
#   all other info for that single 'None' value
############################################################

#           Append,Combine and Joining two series
songs_66=pd.Series([3,None,11,9],index=['George','Paul','John','Ringo'],name='Counts')
songs_69=pd.Series([1,23,55,4],index=['shyam','ram','ganshyam','Radhesham'],name='counts')
songs=songs_66.append(songs_69)
songs

#############################################################

#                       matplotlip
#plotting two series
#This is for line bar representation
import matplotlib.pyplot as plt
fig=plt.figure() #Will open canvas to draw for you
songs_69.plot()    #Draws the graph on values of songs_69(values=[1,23,55,4])
plt.legend()    #pops the graph directly

#---------------------------------------------------------
#This is for Bar graph representation
import matplotlib.pyplot as plt
fig=plt.figure() #Will open canvas to draw for you
songs_69.plot(kind='bar',color='g')    #Draws the graph on values of songs_69(values=[1,23,55,4])
songs_66.plot(kind='bar',color='y')
plt.legend()
#---------------------------------------------------------
#This is for histogram
#Creating seperate series
import numpy as np
data=pd.Series(np.random.randn(500),name='500 random numbers') 
                        #histogram of 500 random numbers
fig=plt.figure()
ax=fig.add_subplot(111) #perfectly aligned on the graph page
data.hist()


############################################################

'''
    DATAFRAMES IN PYTHON
    -upgrade pandas- on base terminal(anaconda navigator), 
    "conda install --upgrade pandas"
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
#Converts feed column to numeric type