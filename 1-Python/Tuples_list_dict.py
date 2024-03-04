# -*- coding: utf-8 -*-
"""
Collections:Tuples,list,set and dictionary

@author: Vishwajeet
"""

#Python Collection Types
'''
#Tuples A Tuple represents a collection of objects that are ordered and immutable
(cannot be modified).
#Lists Lists hold a collection of objects that are ordered and mutable (changeable),
they are indexed and allow duplicate members.
#Sets Sets are a collection that is unordered and unindexed. They are mutable
(changeable) but do not allow duplicate values to be held.
#Dictionary A dictionary is an unordered collection that is indexed by a key
which references a value. The value is returned when the key is provided.
'''
#Creating Tuples
tup1 = (1, 3, 5, 7)
#Accessing Elements of a Tuple
print(f'tup1[0]:\t{tup1[0]}')
print('tup1[1]:\t', tup1[1])
print('tup1[2]:\t', tup1[2])
print('tup1[3]:\t', tup1[3])

#Tuples Can Hold Different Types
tup2 = (1, 'John',  True, -23.45)
print(tup2)
#Iterating Over Tuples
tup3 = ('apple', 'orange', 'plum', 'apple')
for x in tup3:
   print(x)
#Tuple Related Functions
#You can also find out the length of a Tuple
len(tup3)
#You can count how many times a specified value 
#appears in a Tuple 
tup4 = ('apple', 'orange', 'plum', 'apple','apple')
#Tuples allow duplicates;
tup4.count('apple')
#You can also find out the (first) index of a value in a Tuple:
print(tup4.index('apple'))
print(tup4.index('plum'))
#Checking if an Element Exists
if 'orange' in tup3:
   print('orange is in the Tuple')
#Nested Tuples
#Tuples can be nested within Tuples; 
#that is a Tuple can contain, as one of its
#elements, another Tuple.
tuple1 = (1, 3, 5, 7)
tuple2 = ('John', 'Denise', 'Phoebe', 'Adam')
tuple3 = (42, tuple1, tuple2, 5.5)
print(tuple3)
#It is not possible to add or remove 
#elements from a Tuple; they are immutable.
#############################################
#Lists
#Lists are mutable ordered containers of other objects.
#Creating Lists
lst1 = ['John', 'Paul', 'George', 'Ringo']
#As with Tuples we can have nested lists and lists containing different types of
#elements.
lst1 = [1, 43.5, True]
lst2 = ['apple', 'orange', 31]
root_list = ['John', lst1, lst2, 'Denise']
print(root_list)
##########################
#Accessing Elements from a List
lst1 = ['John', 'Paul', 'George', 'Ringo']
print(lst1[-1])
lst1[-1]
lst1[-2]
##################
lst1 = ['John', 'Paul', 'George', 'Ringo']
print('lst1[1]:', lst1[1])
print('lst1[-1]:', lst1[-1])
print('lst1[1:3]:', lst1[1:3])
print('lst[:3]:', lst1[:3])
print('lst[1:]:', lst1[1:])
##########################
#Adding to a List
lst1 = ['John', 'Paul', 'George', 'Ringo']
lst1.append('Pete')
print(lst1)
#You can also add all the items in a list 
#to another list. There are several options
lst1 = ['John', 'Paul', 'George', 'Ringo', 'Pete']
print(lst1)
lst1.extend(['Albert', 'Bob'])
#here, we can use the extend()
lst1
#Inserting into a List
a_list = ['Adele', 'Madonna', 'Cher']
print(a_list)
a_list.insert(1, 'Paloma')
print(a_list)
#List Concatenation
lst1 = [3, 2, 1]
lst2 = [6, 5, 4]
lst3 = lst1 + lst2
print(lst3)
#Removing from a List
another_lst = ['Gary', 'Mark', 'Robbie', 'Jason', 'Howard']
print(another_lst)
another_lst.remove('Robbie')
print(another_lst)
#The pop() Method
#It removes an element from the List; 
#however, it differs from the remove()
#method in two ways:
# It takes an index which is the index of the item to remove from the list rather
#than the object itself.
lst6 = ['Once', 'Upon', 'a', 'Time']
print(lst6)
print(lst6.pop(2))
print(lst6)
#Inserting into a List
a_list = ['Adele', 'Madonna', 'Cher']
print(a_list)
a_list.insert(1, 'Paloma')
print(a_list)
#######################
#List Concatenation
list1 = [3, 2, 1]
list2 = [6, 5, 4]
list3 = list1 + list2
print(list3)
#####################################
#Creating a Set
basket = {'apple', 'orange', 'apple', 'pear','orange', 'banana'}
print(basket)
#When run this code will show that apple is only added once to the set:
#Accessing Elements in a Set
for item in basket:
   print(item)
#################
#Adding Items to set
basket = {'apple', 'orange', 'banana'}
basket.add('apricot')
print(basket)
#If you want to add more than one item to a Set you can use the update() method:
basket = {'apple', 'orange', 'banana'}
basket.update(['apricot', 'mango', 'grapefruit'])
print(basket)
######################
#Obtaining the Length of a Set
basket = {'apple', 'orange', 'apple', 'pear', 'orange','banana'}
print(len(basket))
#Obtaining the Max and Min Values in a Set
basket2={23,45,67,12,456}
print(max(basket2))
print(min(basket2))
#Removing an Item
basket = {'apple', 'orange', 'apple', 'pear', 'orange','banana'}
print(basket)
basket.remove('apple')
basket.discard('apricot')
print(basket)
#Set Operations
s1 = {'apple', 'orange', 'banana'}
s2 = {'grapefruit', 'lime', 'banana'}
print('Union:', s1 | s2)
print('Intersection:', s1 & s2)
print('Difference:', s1 - s2)
############################################
#Dictionaries
#A Dictionary is a set of associations
# between a key and a value that is unordered,
#changeable (mutable) and indexed.
capitals = {
'Maharashtra': 'Mumbai',
'Gujrat': 'Ahmadbad',
'UP': 'Lakhnow',
'Karnataka': 'Banglore',
'Andhrapradesh': 'Hydrabad'
}
print(capitals)
#Accessing Items via Keys
print('capitals[Maharashtra]:', capitals['Maharashtra'])
#Adding a New Entry
capitals['West_Bengal']='Kolkatta'
capitals
#Changing a Keys Value
capitals['Gujrat'] = 'Gandhinagar'
print(capitals)
#Removing an Entry
capitals.pop('Karnataka')
print(capitals)
del capitals['UP']
print(capitals)
#Iterating over Keys
capitals = {
'Maharashtra': 'Mumbai',
'Gujrat': 'Ahmadbad',
'UP': 'Lakhnow',
'Karnataka': 'Banglore',
'Andhrapradesh': 'Hydrabad'
}
for states in capitals:
   print(states, end=', ')
   
for states in capitals:
     print(states, end=', ') 
     print(capitals[states])
#Values, Keys and Items
print(capitals.values())
print(capitals.keys())
print(capitals.items())
########################
#Checking Key Membership
print('Karnataka' in capitals)
print('Bihar' not in capitals)
#Obtaining the Length of a Dictionary
print(len(capitals))
#Dictionaries can have values in tuple
seasons = {'Summer': ('Feb','Mar', 'Apr', 'May'),
'Rainy': ('June', 'July', 'August','Sept'),
'Winter': ( 'Oct','Nov','December', 'January')}
print(seasons['Rainy'])
print(seasons['Rainy'][1])
#Dictionary Methods
#get() is a useful method to access the 
#values of a key in a dictionary.
print(capitals.get('UP'))
#Duplicates Not Allowed
#Dictionaries cannot have two items with the same
# key:
dict2 =	{
  "brand": "Maruti",
  "model": "Breeza",
  "year": 2021,
  "year": 2020
}
print(dict2)
#############################
#Loop Through a Dictionary,it will show only keys
for x in dict2:
  print(x) 
#Print all values in the dictionary, one by one:
for x in dict2:
  print(dict2[x]) 
#You can also use the values() method to return values of a dictionary:
for x in dict2.values():
  print(x) 
#you can use the keys() method to return the keys of a dictionary:
for x in dict2.keys():
  print(x) 
#Loop through both keys and values, by using the items() method:
for x, y in dict2.items():
  print(x, y) 
#Copy a Dictionary
#Make a copy of a dictionary with the copy() method:

mydict = dict2.copy()
print(mydict)
