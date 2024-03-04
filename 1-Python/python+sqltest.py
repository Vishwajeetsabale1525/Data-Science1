# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:52:32 2023

@author: Vishwajeet
"""
#1
import pandas as pd
import numpy as np
d1={'name':['anna','dinu','ramu','ganu','emily','mahesh','jayesh','venkat','ajay','dhanesh']
    ,
    'score':[12.5,16.5,np.nan,9,20,14.5,np.nan,8,19,12],
    'attempts':[1,2,3,4,5,6,7,8,9,10],
    'qualify':['yes','yes','no','yes','yes','no','yes','no','yes','no']
    }
d2=pd.DataFrame(d1)
print(d2)   
labels=['a','b','d','e','f','g','h','i','j','k']
d1=pd.DataFrame(d1,index=labels)
d1
df1=d1.replace(to_replace={'yes':'True','no':'False'})
print(df1)

#2 Q2Write a Python program to plot two or more lines  with different styles. 
import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5]
plt.plot([xi**2 for xi in x ],'o')
plt.plot([xi*2 for xi in x],'--')
plt.plot([xi+3 for xi in x],':')
plt.show()

#4#compute the determinant of a given square array
a=np.array([[1,0],[1,2]])
print(a)
print(np.linalg.det(a))

#5 Q.5 Write a Python function to find the kth smallest element in a list.
l1=[1,2,3,4,5,6,1]
def mini(l1):
    fist=l1[0]
    for i in l1:
        if i<fist:
            fist=i
    print(i)
mini(l1)

#3
arr=np.array([1,2,3])
print(arr)
r1=np.linalg.norm(arr,ord=1)
r1

r2=np.linalg.norm(arr,ord=2)
r2


