# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 09:11:28 2023

@author: Vishwajeet
"""

#ZIP function 
#Use of zip function
# Define two lists: 'name' containing names and 'info' containing corresponding information
name = ['dada', 'mama', 'kaka']
info = [1950, 6032, 9785]

# Loop through both lists simultaneously using the zip function
for nm, inf in zip(name, info):
    # Print each name-info pair obtained from the zip operation
    print(nm, inf)

# In the second example, the 'name' list has an additional element compared to the 'info' list
# This will lead to a mismatch in lengths when using zip
name = ['dada', 'mama', 'kaka', 'baba']
info = [1950, 6032, 9785]

# Loop through both lists simultaneously using the zip function
for nm, inf in zip(name, info):
    # The loop will only iterate through the first three elements of both lists
    # The fourth element in 'name' ('baba') will not have a corresponding 'info' element to pair with
    print(nm, inf)
# Define two lists: 'name' containing names and 'info' containing corresponding information
name = ['dada', 'mama', 'kaka']
info = [1950, 6032, 9785]

# Loop through both lists simultaneously using the zip function
for nm, inf in zip(name, info):
    # Print each name-info pair obtained from the zip operation
    print(nm, inf)

# In the second example, the 'name' list has an additional element compared to the 'info' list
# This will lead to a mismatch in lengths when using zip
name = ['dada', 'mama', 'kaka', 'baba']
info = [1950, 6032, 9785]

# Loop through both lists simultaneously using the zip function
for nm, inf in zip(name, info):
    # The loop will only iterate through the first three elements of both lists
    # The fourth element in 'name' ('baba') will not have a corresponding 'info' element to pair with
    print(nm, inf)


#disadvantage is that it avoids the excess element 
#that solution is zip_longest

#zip_longest function in python
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[1950,6032,9785]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
    
#use of fill value instead of none    
#It will avoid print None in output bul fillfull
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[1950,6032,9785]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
        
#use of all() if all the values are TRUE then it will produce output
lst=[2,3,6,8,9,-2]
if all(lst):
    print('all values are true')
else:
    print('Useless')    
    
#############################################
lst=[2,3,6,8,9,0]
if all(lst):
    print('all values are true')
else:
    print('Useless')    
    
############################################################
#Use of any if any one is positive
lst=[0,0,0,-8,0]
if any(lst):
    print('It has a some value')
else:
    print('Useless')
    
############################################################
#use of any
lst=[0,0,0,0]
if any(lst):
    print('It has a some value')
else:
    print('Useless')
    
##########################################################
#Count
from itertools import count
counter =count()
print(next(counter))
print(next(counter))
print(next(counter))    
    
###########################################################
#Now let us start from 1
from itertools import count
counter =count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))    
    
############################################################
#cycle
#suppose you have repeted tasks to be done, then you can use this method
#temprature,light,huminity
import itertools

instructions=("Eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)
    
############################################################
#repeat()
from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)
    
############################################################
'''
permutations and combination
'''
#combinations
from itertools import combinations
players=['john','Jani','Janardhan']
for i in combinations(players,2):
    print(i)    


###########################################################
#permutations
from itertools import permutations
players=['john','Jani','Janardhan']
for seat in permutations(players,2):
    print(seat)    
#in their all possible combinations are in their 

###########################################################
    
#Product
from itertools import product
team_a = ['Rohit','Pandya','Bumrah']
team_b = ['virat','manish','sami']
for pair in product(team_a,team_b):
    print(pair)
    
#############################################################
#Filter function
age=[27,17,21,19]
adults=filter(lambda age:age>=18,age)
print([age for age in adults])

#############################################################
'''
In python, assignment statement (obj_b = obj_a) do not create real copi
It only creates a new variable 

shallo copy and deep copies
'''
#Assignment opration
#shallo copy and deep copy
#This will only create a new vaariable with the same reference.Modifying 
list_a=[1,2,3,4,5]
list_b=list_a

list_a[6] =-10
print(list_a)
print(list_b)
    
##################################################################
#-------------------------Shallo Copy-----------------------------
##################################################################    
    
#one level deep.modifying on level 1 does not affect the other list.
#Use copu.copy(), or object-specific copy functions/copy constructor
import copy
list_a=[1,2,3,4,5] 
list_b = copy.copy(list_a)

#not affects the other list
list_b[0] = -10
print(list_a)
print(list_b)

'''
Shallow copy is going to create deta object one level deep.
modifying on level 1 does not affect the other list
in order to 1
'''    

#but with nested objects modifying on level 2 or deeper does affect the 
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)

#affect the other!
list_a=[0][0]=-10
print(list_a)
print(list_b)  

#o/p:-10
   # [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)

#affect the other!
list_a=[0][0]=-10
print(list_a)
print(list_b)  

#write python program to create an iterator from sevral iterables 
#in a sequence and display the type and element of the new iterator

from itertools import chain
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
#List
result=chain_func([1,2,3],['a','b','c','d'],[4,5,6,7,8,9])
print('Type of new iterator:')
print(type(result))
print('Elements of the new iterator:')
for i in result:
    print(i)
    
#Tuple
#using tuple
result=chain_func([10,20,30],['A','B','C','D'],[40,50,60,70,80,90])
print('Type of new iterator:')
print(type(result))
print('Elements of the new iterator:')
for i in result:
    print(i)
    
#write pythonn program that genrates the running product of element
#in an iterable.

#recheck this code
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)
    
#################################
#List
result=running_product([1,2,3,4,5,6,7])    
print("Running product of a list:")
for i in result:
    print(i)
    
#Using tuple
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)
    
#################################
#List
result=running_product((1,2,3,4,5,6,7))    
print("Running product of a list:")
for i in result:
    print(i)

    
'''
3.Write a python program to construct an infinte itterators that 
#returnn evenly spaced values starting with a specifieed number and step.

'''    
import itertools as it 
start = 10
step = 1 
print("The starting number is ", start,"and step is",step)
my_counter=it.count(start,step)  
#following loop will run for ever
print('The said function print never-ending items:')
for i in my_counter:
    print(i)
    
##############################################################
    
'''
write python program to genrate an infinite cycle of element 
from an iterable.
'''
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
#following loops will run for ever
#List
result =cycle_data(['A','B','C','D'])
print("The said function print never-endinf items:")
for i in result:
    print(i)    

###############################################################

#String
result=cycle_data('Python itertools')
print("The said function print never-ending items:")
for i in range:
    print(i)

########################################################


'''
write python program to make an iterator that drops elements 
from the iterable as soon as an element is a positive number.
'''
import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x : x< 0,nums)
nums = [-1,-2,-3,-4,-10,2,0,5,12]
print("Original list: ",nums)
result= drop_while(nums)
print("drop elements from the iterable when a positive number arrises \n",list(result))

#Alternative solution 



























    
    
    
    
