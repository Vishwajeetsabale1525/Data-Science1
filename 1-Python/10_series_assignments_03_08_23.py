'''
1.write a pandas program create and display a one dimentional array 
like containing an array of data
'''
import pandas as pd
ds = pd.Series ([2,4,6,8,10])
print(ds)

####################################################
'''
2.Write a pandas program t convert a pandas module series to 
python list and its type
'''
import pandas as pd
ds=pd.Series([2,4,6,8,10])
print('Pandas Series and type')
print(ds)
print(type(ds))
print('Convert Pandas Series to python list')
print(ds.tolist())
print(type(ds.tolist()))

'''
3.Write a pandas program to add, subtract,multiplication and division
sample series =[2,4,6,8,10],[1,3,5,7,9]
'''
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
ds=ds1+ds2
print('Add two Series')
print(ds)
print('Subtract two Series')
ds=ds1-ds2
print(ds)
print('Multiply two Series')
ds=ds1*ds2
print(ds)
print('Divide Series1 by Series two')
ds=ds1/ds2
print(ds)

'''
4. Write a pandas program to compare the elemetn of the series sample series
sample series =[2,4,6,8,10],[1,3,5,7,9]
'''
import pandas as pd
ds1 =pd.Series([2,4,6,8,10]) 
ds2 =pd.Series([1,3,5,7,10])
print('Series1')
print(ds1)
print('Series2')
print(ds2)
print('compare elements:')
print('Equals:')
print(ds1==ds2)
print('Greter than:')
print(ds1>ds2)
print('Less than:')
print(ds1<ds2)

'''
5.Write a pandas program to convert a dictionary to a pandas series
{'a':100,'b:200','c:300','d:400','e:800'}
'''

import pandas as pd
import pandas as pd
d1 = {'a':100,'b':200,'c':300,'d':400,'e':500}
print("Original Dictionary :")
print(d1)
new_series = pd.Series(d1)
print("Converted Series :")
print(new_series)

'''
6.Write a pandas program to convert a Numpy array to a Panda Series
'''

import pandas as pd
import pandas as np
n_a=np.array([10,20,30,40,50])
print('Numpy array:')
print(n_a)
new_series= pd.Series(n_a)
print('Converted pandas series')
print(new_series)

'''
7.Write a pandas program to change the datatype of given a column or a 
seres
'''
#For column use 'loc' and for index use 'iloc'
#Converting dataframe into series, iloc and loc
import pandas as pd
s1=pd.Series(['100','200','Python','300.12','400'])
print('Original Data Series:')
print(s1)
print('Change the solid data type to numeric:')
s2=pd.to_numeric(s1,errors='coerce')
print(s2)

'''
8.Write a pandas program to convert a first column of datafreame 
as series 
'''
#For name of column use 'loc'
#and for index od column use 'iloc'
import pandas as pd
d={'col1':[1,2,3,4,7,11],'col2':[4,5,6,9,5,0],'col3':[7,5,8,12,1,11]}
df=pd.DataFrame(data=d)
print('Original DataFrame:')
print(df)
s1=df.iloc[:,0]   #all rows and 0th column
print('\n1st column as a series:')
print(s1)

'''
#################################################################
'''
import pandas as pd
s=pd.Series([['Red','Green','White'],['Red','Black',],['Yeollo']])
print('Oroginal Series Of List')
print(s)
#s1=s.apply(pd.Series).stack().reset_index(drop=True)
s1=s.apply(pd.Series)
s2=s1.stack()
s3=s2.reset_index(drop=True)
print('One Series')
print(s)

#DataFrame - stack() functions

#The stack function is used to stack the priscribe Level(s) from 
#column to index

#Return a reshaned DataFrame or series


'''
9.Write a pandas program to add some deta to existing series
'''

import pandas as pd
s=pd.Series(['100','200','python','300.12','400'])
print('Oroginal Series Of List')
print(s)
print('\nData series after adding some data:')
new_s=pd.concat([s,pd.Series([500,'php'])], ignore_index=True)
print(new_s)

'''
10.Write a Pandas program to change the order of index of a given 
series
'''

import pandas as pd
s=pd.Series(['100','200','python','300.12','400'])
print('Original Series Of List')
print(s)
print('\nData series after adding some data:')
new_s=pd.concat([s,pd.Series([500,'php'])],ignore_index=True)
print(new_s)

'''
11.Write a pandas program to change the order of index of a given series

'''

import pandas as pd
s=pd.Series(data=[1,2,3,4,5], index=['A','B','C','D','E'])
print('Original Data Series:')
print(s)
s.shape
s=s.reindex(index=['B','A','C','D','E'])
print('Data series after changing the order of index')
print(s)

'''
12.Write a pandas program to 
'''











