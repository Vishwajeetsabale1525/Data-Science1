# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:04:44 2023

@author: Vishwajeet
"""

#write a Numpy program to get numpy vwersion and show the numpy
import numpy as np
print(np.__version__)
####################################################3
#write a NumPy program to test weather
#none of the element of given array are zero
import numpy as np
x=np.array([1,2,3,4])
print("Original array: ")
print(x)
print("Test if none of the elements of the said array is zero: ")
print(np.all(x))
x=np.array([0,1,2,3])
print("Original array")
print(x)
print("Test if none of the elements of the said array is zero: ")
print(np.all(x))

##############################################################33
#write the numpy program to test if any of the element of a given array are non zero
import numpy as np
x=np.array([1,0,0,0])
print("Original Array:")
print(x)
print("Test weather any of the elements of a given array is non-zero:")
print(np.any(x))
x=np.array([0,0,0,0])
print("Original array: ")
print(x)
print("Test weather any of the elements of a given array is non_")
print(np.any(x))

################################################################
'''
write numpy program to test a given array element 
wise for finitness (non infinity or not a number).
'''
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print("original array")
print(a)
print("Test a given array element wise for finitness: ")
print(np.isfinite(a))

###############################################################
'''
write a program to test the element wise for NaN 
of a given array
'''
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print("original array")
print(a)
print("Test a given array element wise for NaN: ")
print(np.isnan(a))

##############################################################3

'''
Write Numpy Program to create element-wise
comparison (greater,greater_equal,less and less_equal)
of two given arrays
'''
import numpy as np
x=np.array([3,5])
y=np.array([2,5])
print("Original no: ")
print(x)
print(y)
print("Comparison- greater")
print(np.greater(x,y))
print("Comparison greater_equal")
print(np.greater_equal(x,y))
print("Comparison-less")
print(np.less(x,y))
print("Comparison-Less_equal")
print(np.less_equal(x,y))
########################################################

#write a Numpy program to create 3*3 identity matrix
import numpy as np
array_2D=np.identity(3)
print("3*3 matrix:")
print(array_2D)
#identity matrix means diagnal shhould be 1

#########################################################3
#Write a Numpy program to generate a random number between 0 and 1

import numpy as np
rand_num=np.random.normal(0,1,2)
print(rand_num)

#######################################################
'''
write numpy program to create 3*4 array and in
iterate over it
'''
import numpy as np
a=np.arange(10,22).reshape((3,4))
print("Original array")
print(a)
print("Each element of the array is: ")
for x in np.nditer(a):
    print(x,end=" ")
    print()


#####################################################33
'''
write a NumPy program to create a vector of length 5 with values
evenly distributed between 10 and 50
'''
import numpy as np
v=np.linspace(10, 49,5)
#10-start point, 49-end point, 5-nos in vector
print("Length 10 with values evenly distributed between 10 to 50")
print(v)

#########################################################3

'''
write numpy program to create a 3*3 matrix
with value ranging from 2 to 10
'''
import numpy as np
x=np.arange(2,11).reshape(3,3)
print(x)

###########################################################
#write numpy program to reverse an array
#(the first element become last).
import numpy as np
x=np.arange(12,38)
print("Original array: ")
print(x)
print("Reverse array: ")
x=x[::-1]
print(x)

'''
1.Write a numpy program to get the NumPy version and show the NumPy
'''
import numpy as np
print(np._version_)

#############################################################

'''
2.Write numpy program to test whether none of the element of a given 
array are zero
'''
import numpy as np
x=np.array([1,2,3,4])
print("Original array:")
print(x)
print('Test if name of the element of the said array is zero:')
print(np.all(x))
x = np.array([0,1,2,3])
print("Original array")
print(x)
print('Test if name of the element of the said array is zero:')
print(np.all(x))

######################################################################
'''
3.Write numpy program to test if any of the element of a 
given array are Non-zero.
'''
import numpy as np
x = np.array([1,0,0,0])
print(x)
print(np.any(x))

import numpy as np
x = np.array([1,0,0,0])
print(x)
print(np.any(x))

#############################################################
'''
4.Write numpy program to test a given array element wise for  finteness
(not infinity or not a number)
'''
#   np.isfinite() ==> to see a finite number present or not
#    if finite number present then output = True
#    if (infinite OR Nan ) present then output = False

import numpy as np
a = np.array([1,0,np.nan,np.inf])
print(a)
print(np.isfinite(a))

#############################################################
'''
5.Write numpy program to test element-wise for "NaN"
of the given array
'''
#   np.isnan() ==> to see a "Nan" present or not
#    if NaN value present then output = True
#    if NaN value Not present then output = False
import numpy as np
a = np.array([1,0,np.nan,np.inf])
print(a)
print(np.isnan(a))

#############################################################
'''
6.Write numpy program to test element-wise coparision
(greater,greater_equal,less and less_equal) of given 2 array
'''
import numpy as pd 
x = np.array([3,5])
y = np.array([2,5])
print(x)
print(y)
print(np.greater(x,y))
print(np.greater_equal(x,y))
print(np.less(x,y))
print(np.less_equal(x,y))

#############################################################
'''
7.Write numpy program to create a 3x3 identity matrix
'''
import numpy as pd 
array_2D = np.identity(4)
print('3x3 matrix:')
print(array_2D)

#############################################################
'''
8.Write numpy program to genrate a number between 0 and 1
'''
import numpy as pd
rand_num = np.random.normal(0,1,1)
print(rand_num)

#############################################################
'''
9.Write a Numpy program to create a 3x4 array and 
iterate over it.
'''
import numpy as np
a = np.arange(10,22).reshape(3,4)
print(a)
for x in np.nditer(a):
    print(x,end=" ")
    print()

#############################################################
''''
10.Write a Numpy program to create a vector of length 10
with values evenly distributed between 5 to 50
'''
#  np.linspace --> called as linespace
#  ( start, end , length of vector)
import numpy as np
v =np.linspace(10,49,5)
print(v)

#############################################################
'''
11.Write a Numpy program to create a 3x3 matrix with value 
ranging from 2 to 10
'''
import numpy as pd
x = np.arange(2,11).reshape(3,3)
print(x)

#############################################################
'''
12.Write a Numpy program to reverse an array 
(the first element becomes the last)
'''
import numpy as np
x=np.arange(1,10)
print(x)
x=x[::-1]
print(x)

#oR
import numpy as np
x = np.arange(1,7)
print(x)
print(np.flip(x))

#############################################################
'''
13.Write a Numpy program to compute the multiplication of two matrix 
'''  #dot product
import numpy as pd
p = [[1,0],[0,1]]
q = [[1,2],[3,4]]
print(p)
print(q)
result1 = np.dot(p,q)
print(result1)

#################################################################
'''
14.Write a Numpy program to compute the cross product 
of given 2 matrix
'''
import numpy as pd
p = [[1,0],[0,1]]
q = [[1,2],[3,4]]
print(p)
print(q)
result1 = np.cross(p,q)
result2 = np.cross(p,q)
print(result1)
print(result2)

####################################################################
'''
15.Write a Numpy program to compute determinant of a given square array
'''
import numpy as np
from numpy import linalg as LA
a = np.array([[1,0],[1,2]])
print(a)
print(np.linalg.det(a))

####################################################################
'''
16.Write a NumPy program to compute eigenvalues and right
eigenvalues of a given square array.
'''
import pandas as pd
m = np.mat("3 -2;1 0")
print("a/n" ,m)
w,v = np.linalg.eig(m)
print("Enginevalue of said matrix",w)
print("Enginevalue of said matrix",v)

'''
17.Write a NumPy program to 
'''



















######################################################
##write a Numpy program to
#compute the determinant of given square







#########################################
#write a program to compute the eigrnvalues  and right eignvectors 
#of a given sqare array
import numpy as np
m=np.mat("3 -2;1 0")
print("Original matrix")
print("a\n",m)
w,v=np.linalg.eig(m)
print("Eignvalues of the said matrix",w)
print("Eignvectors from said matrix",v)

###############################################
#write a program to compute the inverse of a given 
#matrix
import numpy as np
m=np.array([[1,2],[3,4]])
print("Original matrix: ")
print(m)
result=np.linalg.inv(m)
print("Inverse of the said matrix:")
print(result)
