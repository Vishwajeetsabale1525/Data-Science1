##########################################################################
#-----------------------------08-08-23-----------------------------------#
##########################################################################

import pandas as pd
import numpy as np
technologies={'Courses':['Spark','Pyspark','Hadoop','Python','Pandas'],
              'Fee':[20000,12000,35000,10000,23000],
              'Duration':['30Days','40Days','20Days','90Days','45Days'],
              'Discount':[12,34,21.8,10,20]}
df=pd.DataFrame(technologies)
df

#Pandas.DataFrame.query() by examples 
#Query all with courses equals 'Spark'
df2=df.query("Courses=='Spark'")
print(df2)

##################################################

#Not equals condition
df2=df.query('Courses'!='Spark')
print(df2)

##################################################

import pandas as pd
import numpy as np
technologies={'Courses':['Spark','Pyspark','Hadoop','Python','Pandas'],
              'Fee':[20000,12000,35000,10000,23000],
              'Discount':[12,34,21.8,10,20]}
df=pd.DataFrame(technologies)
print(df)

#Pandas add column to dataframe
#Add new column to dataframe
tutors=['Ram','Sham','Ghansham','Ganesh','Ramesh']
df2=df.assign(TutorsAssigned=tutors)
print(df2)

###############################################

#Add multiple columns to dataframe
MNCCompanies=['Tata','HCL','Infosys','IBM','Google']
df2=df.assign(MNC=MNCCompanies,tutors=tutors)
df2

################################################

#Derive new columns from existing columns
df=pd.DataFrame(technologies)
df2=df.assign(Discount_Percent=lambda x:x.Fee*x.Discount/100)
print(df2)

##############################################

#Append columns to existing pandas dataframe
#Add new column to the exiting dataframe
df=pd.DataFrame(technologies)
df['MNCCompanies']=MNCCompanies
print(df2)

###############################################

#Add new column at the specific position
df=pd.DataFrame(technologies)
df.insert(0,'Tutors',tutors)
print(df)


###############################################################

#Quick examples of get the number of rows in dataframe
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count
column_count=len(df.axes[1])
column_count

############################################################

df=pd.DataFrame(technologies)
row_count=df.shape[0]   #Returns number of rows
col_count=df.shape[1]   #Returns number of columns
print(row_count)
print(col_count)