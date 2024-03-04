# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:26:36 2023

@author: Vishwajeet
"""

lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

#we can write same code using list comprensiion
lst =[num for num in range(0,20)]
print(lst)

###############################################################
names = ['dada','kaka','mama']
lst = [name.capitalize() for name in names]
print(lst)

########################################################

def is_even(num):
    return num%2==0
lst = [num for num in range (10) if is_even(num)]
print(lst)

#min, max,palindrome,vovels by list comprenstion

###################################################5####

lst = [f"{x}{y}"for x in range(3) for y in range(3)]
print(lst)

#set comprenstion
lst ={x for x in range(20)}
print(lst)

#######################################################
#Dictionsry comprension
dict = {x:x*x for x in range(3)}
print(dict)

########################################################

#Genrator
#It is another way to creating iterators
#in a simple way where 
#It uses the keyword "yiled"
#                  ===========
#instead of returning it in a defined function
#genrators are implemented using a function


gen=(x for x in range(3))
print(gen) #------------>object is created here
for num in gen:
    print(num)
    
###################################################
#another way of accesing values from object is generator
gen=(x for x in range(3))
next(gen)
next(gen)
next(gen)

###########################################################

def range_even(end):
    for num in range (0,end,2):
        yield num
for num in range_even(6):  #--->this for loop is use 
                                   #to multiple values
    print(num)

#now instead of using for loop we can write our own genrator
gen=range_even(6)
next(gen)  #--->0
next(gen)  #--->2
next(gen)  #--->4
next(gen)  #--->stop itretion

############################################################
#Changing genrator
def lengths (itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
        
passwords=["not-good","give'm-pass","00100=100"]
for password in hide(lengths(passwords)):
    print(password)

############################################################
#Enumerate
#printing list with index
lst=["milk","Egg","Bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')
############
#same code can be implemented using enumerate
lst=["milk","Egg","Bread"]
for index,item in enumerate(lst,start=1):
    print(f'{index} {item}')

##########################################################







#################################
#homework
def lengths (itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
import string
adjectives=['sleepy','slow','smelly','wet','fat','red','orange','yellow','green']
nouns=['apple','dinosaur','ball','toaster','goat','dragon','hammer','duck','panda']
import random
adjectives=random.choice(adjectives)
nouns=random.choice(nouns)
#Select number
number = random.randrange(0,100)
#select special character
special_char = random.choice(string.punctuation)
#create new secure password
passwords = adjectives + nouns + special_char + str(number)
print(passwords)
for password in hide(lengths(passwords)):
    print(password,end=" ")
    
    
    
#############################################

#find all numberas in 1 to 1000 divisible  by 7 using list comprention
def find_numbers_divisible_by_7():
    divisible_by_7 = []
    for num in range(1, 1001):
        if num % 7 == 0:
            divisible_by_7.append(num)
    return divisible_by_7

numbers_divisible_by_7 = find_numbers_divisible_by_7()
print(numbers_divisible_by_7)

##########################################################

div1 = [n for n in range(1,1000) if n% 7==0]
print(div1)

#######################
####################
#find all the numbers 1 to 1000 that have number 3 in their using list comprehntion

three = [n for n in range(1, 1001) if '3' in str(n)]
print(three)

#####################################################

#count the  number of spaces in the string
some_strings="the slow the slid aquid swam sumptuously through the slimy"
spaces =[s for s in some_strings if s==' ']
print(len(spaces)) 

#create a list of all consonants in the string 
#"Yello Yeks like yelling and Yawning and yesterday they youled while eatingyuky yams

sentence ="Yello Yaks like yelling and Yawning while eating "
results = [letter for letter in sentence if letter not in 'a,e,i,o,u," "']
print(results)

#find the common numbers in two lists(without using a tuple or set)list
list_a=[1,2,3,4]
list_b=[2,3,4,5]
common=[a for a in list_a if a in list_b]
print(common)

#####################################################
#Get only numbers in a sentence like 'in 1984 there were 13 instances of a protest
sentence="In 1984 there were 13 instances of a protest with over 1000 people attending"
words = sentence.split()
result=[number for number in words if not number.isalpha()]
print(result)

################################################## 

#Given number in the list should be added with even
result =[]
for n in range(20):
    if n%2==0:
        result.append('even')
    else:
        result.append('odd')
print(result)

#######################################
#using list comprention
result=['even' if n%2==0 else 'odd' for n in range(20)]
print(result)

########################################################

#produced list of tuple consisting of only the matching numbers in 
#the list_a=[1,2,3,4,5,6,7,8,9], list_b=[2,7,1,12]. Result would like (4,4),(12,12)

list_a=[1,2,3,4,5,6,7,8,9] 
list_b=[2,7,1,12]
result =[(a,b) for a in list_a for b in list_b if a==b]
print(result)

#homework
#matching words 
#find all the words in a stringn that are less than 4 letters
# 
sentence='on a summer day Ramnath sonar wend'
examine= sentence.split()
result=[word for word in examine if len(word)<=4]
print(result)

##############################################################
#write python program to print  a specified list
# after emoving the 0th ,4th,5th element103

colour =['Red','Green','White','Black','Pink']
colour=[x for(i,x) in enumerate (colour) if i in (0,4,5)]
print(colour)

##############################################################

#Write python program that create a genrator function that yield 
# a cube of numbers from 1 to n accept n from user 

def cube_genrator(n):
    for i in range(1,1+n):
        yield i**3
#accept input from user
n=int(input("Enter a number:"))

#create the genrator object
cubes = cube_genrator(n)
for num in cubes :
    print(num)

############################################################
#write a python program to implement a genrator a genrator that genrates 
# random numbers within a given range

import random
def random_number_genrator(start,end):
    while True:
        yield random.randint(start,end)
        
#accept input from user 
start=int(input("Enter start:"))
end=int(input("enter end:"))
random_number =random_number_genrator(start,end)
print("Random number between",start,"and",end)
for _ in range(10):
    print(next(random_number))

######################################################
#1 dimentional also 2 and 3
#4diamentional 
#write a python program to genrate a 3*4*6 3D array whose each element is*
array=[[['*' for col in range(6)] for col in range(4)]for row in range(3)]
print(array)

#########################################################
#write python program to print the number of specified list after 
#  removing even number from it.
num = [7,8,120,25,44,27]
num = [x for x in num if x%2!=0]
print(num)














































































































































































































































































