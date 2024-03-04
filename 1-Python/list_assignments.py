# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:33:23 2023

@author: Vishwajeet
"""
def sum(list):
    res=0
    for i in list:
        res=res+i
    print(res)
print(sum([2,3,4]))













#write python program to add all the items in the list

#st1[2,3,5,7,8]
def sum_list(sum_list):
    sum=0
    for x in sum_list:
        sum=sum+x
    return sum
print(sum_list([5,6,-8]))

#write python program to multiply all the items in the list

def mul_num(num):
    mult=1
    for i in num:
        mult=mult*i
    return mult
lst2=[1,2,3,4,5]
print(mul_num(lst2))

#write python program to get the largest number from the list
lst1=[1,2,3,4,5,6,7,8]
print(max(lst1))

#write python program to get the smallest number from the list
lst1=[1,2,3,4,5,6,7,8]
print(min(lst1))

# write python program to count the number of string which 
# satisfies the condition that the string length is 2 or 
# more and the first and last character are the same 
# from a given list of strings.given a list
#lst5=['abc','xyz','aba','1221']

def match_words(words):
    ctr = 0
    for word in words:
        if len(word)> 2 and word[0] == word[-1]:
            ctr +=1
    return ctr
print(match_words(['abc','xyz','aba','1221']))

# write a python program to get a list, sorted in incresing 
# order by the element in each tuple from a given list 
# of non-empty tuples.
# sample list : [(2,5),(1,2),(4,4),(2,3),(2,1)]
# expected result : [(2,1),(1,2),(2,3),(4,4),(2,5)]

def last(n):
    return n[-1]
def sort_list_last(tuples):
    result=sorted(tuples,key=last)
    return result
lst1=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print(sort_list_last(lst1))

##################################################
a = [10,20,30,20,10,50,60,40,80,50,40]
dup_items=set()
uniq_items=[]
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)

list1=[2,3,1,2,3,4,5]
st1=set(list1)
print(st1)
st2=list(st1)
print(st2)
# ---------------OR-------------------

lst1=[10,20,30,20,10,50,60,40,80,50,40]
st1= set(lst1)
print(st1)
lst2=list(st1)
print(lst2)

#write a python program to clone or copy a list.
original_list = [10,20,30,40]
new_list = list(original_list)
print(original_list)
print(new_list)

#--------------------------------------------------------#
# Write python program to find the list of list of words that 
#  are longer than n from a given list of words

def long_words(n,str):
    word_len=[]
    txt=str.split(" ")
    for x in txt:
        if len(x)>n:
            word_len.append(x)
    return word_len
print(long_words(3,"The quick brown fox jumps over the lazy dog"))

#write a python function that takes two lists and return 
# trueif they have at least one common member

def common_data(list1,list2):
    result=False
    for x in list1:
        for y in  list2:
            if x==y:
                result=True
                return result
print(common_data([1,2,3,4,5],[5,6,7,8,9]))
print(common_data([1,2,3,4,5],[6,7,8,9]))

#write python program to calculate diffrence between two lists
list1 = [1,3,5,7,9]
list2 = [1,2,4,6,7,8]
diff1= list(set(list1)-set(list2))
diff2= list(set(list2)-set(list1))
total_diff =diff1+diff2
print(diff1)
print(diff2)
print(total_diff)
';'
#write python program to convert a list of character into a string
s =['a','b','c','d']
str1 =''.join(s)
str2 =' '.join(s)
print(str1)
print(str2)

#write a python program to find the index of an item in a 
# specific list
num = [10,30,4,-6]
print(num.index(30))

#write a python program to append a list to the second list
list1=[1,2,3,0]
list2=['Red','Green','Black']
final_list = list1 + list2
print(final_list)






















list1=[1,2,3,4]
list2=['a','b','c','d']
list3=list1+list2
print(list3)

list=[1,2,3,4,5]
print(list.index(3))




