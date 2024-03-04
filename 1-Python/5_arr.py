# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:30:58 2023

@author: Vishwajeet
"""

import numpy as np
#array in numpy
#create nd array
arr=np.array([10,20,30])
print(arr)

#output
#[10 20 30]

#create muktidimensional array
arr=np.array([[10,20,30],[40,50,60]])
print(arr)

#represent minimum dimension
#use ndmin param to specify how many minimum
#dimensions u wanted to create and areay with
arr=np.array([10,20,30,40],ndmin=3)
print(arr)


#change the datatype
#dtype parameter
arr=np.array([10,20,30],dtype=complex)

#dimension of array
arr=np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12]])
print(arr.ndim)
print(arr)

#################################################
#finding the size of the array
arr=np.array([10,20,30])
print("Each item contains in bytes: ",arr.itemsize)
#Each item contains in bytes:  4

#######################################################
#get shape and size of array
arr=np.array([[10,20,30,40],[60,70,80,90]])
print("Array Size: ",arr.size)
print("Shape: ",arr.shape)
#Oputput
'''
Array Size:  8
Shape:  (2, 4)
'''

#########################################################

#create sequence of Integer using arrange()
arr=np.arange(0,20,3)
print("Print sequential array with steps of 3: \n",arr)
#output
'''
Print sequential array with steps of 3: 
 [ 0  3  6  9 12 15 18]
 
'''

#access single element
arr=np.arange(11)
print(arr)    #[ 0  1  2  3  4  5  6  7  8  9 10]

print(arr[2])  #2

print(arr[-2])  #9


#######################################################
#Multi-dimensional array indexing
arr=np.array([[10,20,30,40,50],[50,60,70,80,30]])
print(arr)

print(arr.shape)
print(arr[1,1])
print(arr[0,4])

print(arr[1,-1])
#30

######################################################3
#access array element using slicing
arr=np.array([1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]


x=arr[-2:3:-1]
print(x)  #[8 7 6 5]


x=arr[-2:10]
print(x)  #[8 9]



#indexing in numpy
arr=np.array([[10,20,30,40],
              [40,50,60,70],
              [60,10,70,80],
              [30,90,40,80]])
arr

#Slicing arrayy
#For multidimensional numpy array
#you can accss the element as below

arr[1,2]
arr[1,:]  #to get value of row one and all col
arr[:,1]  #to get all rows and col 1

x=arr[:3,::2]    #Al rows three col, in all selected rows

#Integer array indexingg

arr=np.arange(35).reshape(5,7)
print(arr)
'''
[[ 0  1  2  3  4  5  6]
 [ 7  8  9 10 11 12 13]
 [14 15 16 17 18 19 20]
 [21 22 23 24 25 26 27]
 [28 29 30 31 32 33 34]]
'''


#Boolean array indexing
#this advanced indexing occurs when an object
#it is array object of boolean 
#such as may be returned from comparison operators
#from array which satisfy som cond

arr=np.arange(12).reshape(3,4)
print(arr)

rows=np.array(False,True,True)
wanted_rows=arr[rows,:]
print(wanted_rows)

#create array
arr=np.array([10,20,30,40])
print(arr)
print(type(arr))

#convert list
ist=arr.tolist()
print(ist)
print(type(ist))


#convert multidimensional array to list
#create array
array=np.array([[10,20,30,40],
                [50,60,70,80],
                [60,40,20,10]])
print("Array: ",array)


#convert list
lst=array.tolist()
print("List :",lst)

#convert python list to numpy array
'''
provide two function
1.numpy array()
2.numpy.asarray()

#create list
'''

list=[20,30,40,50]
array=np.array(list)
print("Array:",array)
print(type(array))


#numpy array properties


#shape
array=np.array([[1,2,3],[4,5,6]])
array.shape=(3,2)
print(array)


#resize the arrayy

#reshape usage
array=np.array([[10,20,30],[40,50,60]])
new_array=array.reshape(3,2)
print(new_array)

