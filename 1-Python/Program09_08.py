# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 13:28:10 2023

@author: Vishwajeet
"""

import pandas as pd
import numpy as np
data={'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]}
df=pd.DataFrame(data)
print(df)

def add_3(x):
    return x+3
df2=df.apply(add_3)
df2

#########################OR###########################
df3=((df.A).apply(add_3))
df3

##############################################
#using apply function to single column
def add_4(x):
    return x+4
df["B"]=df["B"].apply(add_4)
df["B"]

##########################################################
# apply to multiple columns
df[['A','B']]=df[['A','B']].apply(add_4)
df[['A','B']]


#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
# apply lambda function to the each column
df2=df.apply(lambda x: x+10)
df2

#################################################################3
#apply function on selected list of multiple columns
df2=df[['A','B']].apply(lambda x: x+7)
df2

###################################################################
#using pandas,Dataframe.transform() to apply function column
# using Dataframe.Transform()
def add_2(x):
    return x+2
df=df.transform(add_2)
print(df)


##################################################################
#using pandas .Dataframe.map() to single column
df['A']=df['A'].map(lambda x: x+3)
df["A"]


##################################################################
#apply library functions
df=pd.DataFrame(data)
df2=df[['A','B']].apply(np.square)
df2

#################################################################
#using numpy.square() Method
df['A']=np.square(df['A'])
df['A']

##################################################################
technologies={'cources':['sparks','pysparks','hadoops','java','cpp','sparks','java'],'fees':[20000,30000,40000,50000,60000,20000,50000],'duration':['30days','31days','32days','33days','34days','30days','33days'],'discount':[11.8,12.8,13.9,14.1,16,11.8,14.1]}
df=pd.DataFrame(technologies)
df

df2=df.groupby(['cources']).sum()
df2


#############################################################################
#group by multiple columns
df2=df.groupby(['cources','duration']).sum()
df2


# add index to grouped data
#add row index to the group by 
df2=df.groupby(['cources','duration']).sum().reset_index()
print(df2)



#pandas get column names from dataframes
import pandas as pd
import numpy as np
technologies={'courses':['sparks','pysparks','hadoops','java','cpp','sparks','java'],
              'fees':[20000,30000,40000,50000,60000,20000,50000],
              'duration':['30days','31days','32days','33days','34days','30days','33days'],
              'discount':[11.8,12.8,13.9,14.1,16,11.8,14.1]}

df=pd.DataFrame(technologies)
print(df)

#get the list of all column names from headers
df.columns
#shuffle the dataframe rows and return all rowa
df1=df.sample(frac=0.5)
print(df1)
##############################################3
#create new index starting from 0
df1=df.sample(frac=1).reset_index()
print(df1)
###########################################3
#Drop shuffle indexx




####################################################
###Joins####
import pandas as pd
###first dataframe
technologies={
             'Courses':["Spark","Pyspark","Python","Pandas"],
             'Fee':[20000,25000,22000,30000],
             'Duration':['20days','30days','15days','50days']}
df=pd.DataFrame(technologies)
#for labelling
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_labels)
######2nd dataframe
technologies2={
             'Courses':["Spark","java","Python","Go"],
             'Fee':[2000,2300,1200,2000]}
df=pd.DataFrame(technologies2)

####labelling
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_labels2)
#####################################################

#pandas inner join mostly used join
#it is used to join two dataframes on indexes
#when indexes don't match the row get dropped from the both the dataframes
################################################3

#pandas join by default it will join the table left join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)
'''
index Courses_left    Fee  Discount_left Courses_right  Discount_right
0      3       Python  10000           10.0           NaN             NaN
1      1      Pyspark  12000           34.0           NaN             NaN
2      4       Pandas  23000           20.0           NaN             NaN
3      2       Hadoop  35000           21.8           NaN             NaN
4      0        Spark  20000           12.0           NaN             NaN
'''
####################################################
#inner join
#Return matching records only
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='inner')
print(df3)

####################################################
#left join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='left')
print(df3)

#######################################################
#right join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='right')
print(df3)

#################################################
#Pandas joins on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how="inner")
print(df3)
#pandas join on col
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how="left")
print(df3)



#######################################################
#pandas merge dataframes
df3=df1.merge(df2)
print(df3)

#####################
#concat
df=pd.DataFrame({"Courses":['java','C','C++','Pandas'],
                 "Fee":[20000,250000,22000,24000]})
df1=pd.DataFrame({'Courses':['Pandas','Hadoop','Hyperion','java'],
                  'Fee':[25000,15200,24500,24900]})
#using concat 
data=[df,df1]
df2=pd.concat(data)
df2

########################################################
#concating multiple dataframes
df=pd.DataFrame({"Courses":['java','C','C++','Pandas'],
                 "Fee":[20000,250000,22000,24000]})
df1=pd.DataFrame({'Courses':['Pandas','Hadoop','Hyperion','java'],
                  'Fee':[25000,15200,24500,24900]})
df2=pd.DataFrame({'Duration':['30day','40day','35day','60day','55day'],
                  'Discount':[1000,2000,2500,2004,3000]})
#concatingg
df3=pd.concat([df,df1,df2])
print(df3)


#######################################################
#Write dataframe to csv file with default params
