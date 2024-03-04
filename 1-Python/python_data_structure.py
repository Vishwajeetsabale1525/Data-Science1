# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:38:00 2023

@author: Vishwajeet
"""

#Python collection type
#Tuple
#list
#Dictionary
#set

#creating tuples
tup1 = (11,3,5,7)
#accessing element of a tuple
print(f'tup1[0]:\t{tup1[0]}')
print('tup[1]:\t', tup1[1])
print('tup[2]:\t', tup1[2])
print('tup[3]:\t', tup1[3])

#Tuple can hold diffrent types
tup2 =(1,'John',True,-23.45)
print(tup2)

#Iterating over tuple
tup3= ('apple','orange','pulm','apple')
for x in tup3:
    print(x)
    
#tuple releted function
#you can also find lenth of tuple using len function
len(tup3)

#you can count how many times a specific value
#appered in a tuple
tup4= ('apple','orange','plum','apple','apple')
#tuple allow duplicate
tup4.count('apple')
#you can also find out the (first) index of a value in a tuple:

    


#cheking if an element exit
if 'orange' in tup3:
    print('orange is in the tuple')

#holy python.com
#hacker rank
#hacker earth
#w3 scholl


#Nested tuple
#tuple can neassted within tuples
#that is a tuple can contain,as one of its
#element,another tuple.
tuple1 = (1,3,5,7)
tuple2 = ('prajwal','abhi','sahil','aniket')
tuple3 = (42,tuple1,tuple2,5.5)
print(tuple3)

#It is not possible to add or remove element
#element from a tuple they are immutable.
####################################################


#LIST
#list are mutable ordered containers of other objects
#creating list
lst1=['john','paul','george','ringo']
#as with tuple we can have neasted lists and lists 
# containing diffrent element
lst1 = [1,43.5,True]
lst2 = ['apple','orange','31']
root_list = ['john','lst1','lst2','Denise']
print(root_list) 
########################################################
#accesing a element from a list
lst1= ['john','paul','george','ringo']
print(lst1[-1])
lst1[0]
lst1[-2]

##########################################################
#index
lst1=['John','Paul','George','Ringo']
print('lst1[1]:',lst1[1])
print('lst1[-1]:',lst1[-1])
print('lst1[1:3]:',lst1[1:3])
print('lst1[:3]:',lst1[:3])
print('lst1[1:]:',lst1[1:])

#############################################
#Adding to a list
lst1=['John','Paul','George','Ringo']
lst1.append('Pete')
print(lst1)

#you can also add element
lst1=['John', 'Paul', 'George', 'Ringo', 'Pete']
print(lst1)
lst1.extend(['Albert','Bob'])
lst1

#---------------------------------------------------------

#inserting into a list
a_list = ['Adele','Madonna','Cher']
print(a_list)
a_list.insert(1,'Paloma')
print(a_list)

#---------------------------------------------------------

#List concatanation
++print(lst3)

#removing from a list

#---------------------------------------------------------#

#--------------------assignments--------------------------# 

#---------------------------------------------------------#

#assignment no.1)
#  take 5 number in a list and find of minimum of the list
#  and maximum of the list
lst1=[1,2,3,4,5]
print(max(lst1))
print(min(lst1))

###########################################################

#2)take 5 strings in the list and make it reverse 
lst1=['om','sai','ram','sham','shiv']
rev=lst1[::-1]
print(rev)

#---------------------------------------------------------#

def reverse_strings_in_list(strings_list):
    return [string[::-1] for string in strings_list]

strings_list = ['om','sai','ram','sham','shiv']
reversed_list = reverse_strings_in_list(strings_list)
print(reversed_list)

#---------------------------------------------------------#

#3)take 10 numbers in the list write script to search for a value

lst3=[21,35,47,65,59,72,61,49,96,85]
x=int(input("Enter Number :"))
if x in lst3:
    print("YES Present")
else:
    print("NOT present")

#---------------------------------------------------------#
lst1=[1,5,7,8,3,9,0,8,3,5]
print(70 in lst1)


#---------------------------------------------------------#

#4)take 10 numbers in the list insert some duplicate number 
#  write script to find duplicate


###########################

lst4=[21,35,47,21,59,72,61,49,59,85]
unique=[]
duplicate=[]
for i in lst4:
    if i not in unique:
        unique.append(i)
    elif i not in duplicate:
        duplicate.append(i)        
print(duplicate)

########################################################

#5)take vovells in the list and non vovells letters find the 
#  total numbers of the vovels in the list

def count_vowels(letters_list):
    vowels = "AEIOUaeiou"
    vowel_count = 0

    for letter in letters_list:
        if letter in vowels:
            vowel_count += 1

    return vowel_count

# Example usage:
    
letters_list = ['a', 'b', 'e', 'f', 'i', 'o', 'z', 'A', 'Z']
vowel_count = count_vowels(letters_list)
print("Total number of vowels in the list:", vowel_count)


lst3=[21,35,47,65,59,72,61,49,96,85]
x=int(input("Enter Number :"))
if x in lst3:
    print("YES Present")
else:
    print("NOT present")

#----------------------------------------------------#

def count_vowels(word):
    vowels="aeiou"
    return sum(1 for char in word if char in vowels)

lst1=['Abhi','Sahil','Swayam','Prajwal']

b=0
for word in lst1:
    b += count_vowels(word)
print("Total number of vowels in the list:", b)




#removing from a list
another_lst = ['gray','mark','om','sai','ram']
print(another_lst)
another_lst.remove('mark')
print('another_lst')

#pop() method

lst6=['once','upon','a','time']
print(lst6)
print(lst6.pop(1))
print(lst6)

#inserting into the list




#---------------------------------------------------------#

#-----------------------------set-------------------------#

#---------------------------------------------------------#


#dont allow duplicate entity
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)

#accesing a element in a set
for item in basket:
    print(item)
    
############################################
#adding item to a set
basket={'apple','orange','banana'}
basket.add('apricot')
print(basket)

#add multiple item in a set
basket={'apple','orange','banana'}
basket.update(['apricot','mango','sai'])
print(basket)

#obtaning the lenth of set
basket={'apple','orange','apple','pear','orange','banana'}
print(len(basket))
#print(basket)

#obtaning a max and min value in a set
basket2={23,45,6,7,8,84,3,322,}
print(max(basket2))
print(min(basket2))

#removing an item
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)
basket.remove('apple')
basket.discard('orange')
print(basket)

##########################################################
#set oprations

s1 = {'apple','orange','banana'}
s2 = {'graps','lime','banana'}
print('Union:',s1 | s2)
print('Intersection:',s1 & s2)
print('Diffrence:',s1 - s2)

################################################

#---------------------------------------------------------#

#----------------------Dictionary-------------------------#

#---------------------------------------------------------#

#ordered ,changable,not allow duplicate

capitals = {'Maharastra':'Mumbai',
            'Gujrat':'ahmdabad',
            'UP': 'Lakhnow',
            'Karnataka': 'Banglore',
            'Andhrapradesh' : 'Hydrabad'
            }
print(capitals)

#accesing items via keys
print('capitals[Maharastra]:',capitals['Maharastra'])

#adding a new entry
capitals['West_Bengal']='Kolkatta'
capitals

#changing a key value
capitals['Gujrat']='Gandhinagar'
print(capitals)
     
#removing an entry
capitals.pop('Karnataka')
print(capitals)
del capitals['UP']
print('capitals')

#itrating over keys
capitals={'Maharashtra':'Mumbai',
          'Gujrat':'Ahmedabad',
          'UP':'Lucknow',
          'Kartanaka':'Banglore',
          'Andrapradesh':'Hydrabad'}
for states in capitals:
    print(states,end=', ')
for states in capitals:
    print(states,end=', ')
    print(capitals[states])
    
#values,keys and item
print(capitals.values())
print(capitals.keys())
print(capitals.items())

#cheking key membership
print('Karanatka' in capitals)
print('Bihar' not in capitals)
print(len(capitals))

#Dictionary can have values in tuple
seasons = {'summer': ('Feb','Mar','Apr','May'),
           'Rainy': ('June','July','August','Sept'),
           'Winter' : ('Oct','Nov','Dec','Jan')}
print(seasons['Rainy'])
print(seasons['Rainy'][0])

#Dictionary methods
#can not have duplicate
#cannot have 2 items with
#dictionary can not have items with the same key
#get()

dict2={"brand":"Maruti",
       "Model":"Breeza",
       "year":2021,
       "year":2020}
print(dict2)

#####################################
#loop thr a dictionary it will show only keys
for x in dict2:
    print(x)
#print all values in dictionary one by one






