# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 14:06:09 2023

@author: Vishwajeet
"""
#write a pandas program to create one dimensional array like
#containing array of data
import pandas as pd
ds=pd.Series([2,4,6,8,10])
print(ds)
#####################################3
#write pandas program to convert a pandas module series 
#to python list and its types
import pandas as pd
ds=pd.Series([2,4,6,8,10])
print("Pandas series and its types")
print(ds)
print(type(ds))
print("Convert pandas series to python list")
#tolist() use for converting series into list
print(ds.tolist())
print(type(ds.tolist()))

##############################################
#write pandas code to add,substract,multiply,divisionn
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
ds=ds1+ds2
print("Addition")
print(ds)
print("Substraction")
ds=ds1-ds2
print(ds)
print("Multiplication")
ds=ds1*ds2
print(ds)
print("Division")
ds=ds1/ds2
print(ds)
print(ds)
##############################################
#write a code to convert to compare the element of the
#of series
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
print("Series1:")
print(ds1)

print("Series2:")
print(ds2)
print("Compare the element to series:")
print("Equals:")
print(ds1==ds2)
print("Greater than: ")
print(ds1>ds2)
print("Lesss than: ")
print(ds1<ds2)
print("Not equal to")
print(ds1!=ds2)
##############################################
#write pandas program to convert a dictionary to 
#a pandas series
import pandas as pd
d1={'a':100,'b':200,'c':300,'d':400,'e':500}
print("Original Dictionary")
print(d1)
new_Series=pd.Series(d1)
print("Converted series")
print(new_Series)
#############################################
#write pandas program program to convert numpy arrays
#to pandas series
import numpy as np
import pandas as pd
na=np.array([10,20,30,40,50])
print("Numpy Array:")
print(na)
new_series=pd.Series(na)
print("Converted pandas Series:")
print(new_Series)
###############################################
#write pandas program to change datatype of given pandas series
# col to series
import pandas as pd
s1=pd.Series(['100','200','python','300.12','400'])
print("Original Data Series: ")
print(s1)
print("Chande said datatype to numeric datatype")
s2=pd.to_numeric(s1,errors='coerce')
print(s2)
##############################################
#write pandas program to convert 
#first colum  of a dataframe series
import pandas as pd
d={'col1':[1,2,3,4,5,6],
   'col2':[7,3,8,9,11,9],
   'col3':[7,5,6,4,1,0]
   }

df=pd.DataFrame(data=d)
print("Original Dataframe")
print(df)
s1=df.iloc[:,0]
print("List col as series")
print(s1)

###############################################

import pandas as pd
s=pd.Series([
    ['Red','Green','Yellow'],
    ['black','white'],
    ['Yellow']
    ])
print('Original series of list')
print(s)
s1=s.apply(pd.Series)
s2=s1.stack()
s3=s2.reset_index(drop=True)
print("One Series")
print(s3)
########################################
#write pandas program to change datatype of given pandas series
# col to series
import pandas as pd
s=pd.Series(['100','200','python','300.12','400'])
print("Original data science:")
print(s)
print("\nData series after adding some data:")
new_s=pd.concat([s,pd.Series([500,"php"])],ignore_index=True)
print(new_s)
#########################################
#write pandas program to sort a given series

import pandas as pd
s=pd.Series(['100','200','python','300.12','400'])
print("Original data science:")
print(s)
new_s=pd.Series(s).sort_values()
print(new_s)
##############################################
#changing the index of series
import pandas as pd
s=pd.Series(data=[1,2,3,4,5],index=['A','B','C','D','E'])
print("Original data series")
print(s)
s=s.reindex(index=['B','A','D','C','E'])
print("Data series after changing the order of series:")
print(s)

import pandas as pd
ds=pd.Series([2,4,6,7,8,'php',3])
new_s=pd.Series(ds).sort_values()
print(new_s)
print(ds)
d1=pd.concat([ds,pd.Series([200,'php'])],ignore_index=True)
d1


import pandas as pd
ds=pd.Series([1,2,3,3,4],index=['a','b','c','d','e'])
ds
ds=ds.reindex(index=['A1','B1','C','D','E'])
ds


