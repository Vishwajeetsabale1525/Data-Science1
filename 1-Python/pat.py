# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:22:42 2023

@author: Vishwajeet
"""

#Tokenization
txt='welcome to the new year 2023'
x=txt.split()
print(x)

######################################
#Removing special characters
import re
def remove_special_characters(text):
    pat=r'[^a-zA-Z0-9.,!?:;\"\'\s]'
    return re.sub(pat,'',text)
#call function
remove_special_characters('077 Not sure if this % was #fun! 558923 What do# you think** of it.? $500USD! ')

txt='welcome: to the, new year;2024!'
x=re.split(r'(?:,|;|\s)\s*')

#######################################
#Removing punctuation
import string
def remove_punctuation(text):
    text=''.join([c for c in text if c not in string.punctuation])
    return text
remove_punctuation('Article: @First sentences of some,{important} article having lot - punctuation. And another one;!')

###############################################
#Streaming
'''
streaming is used for reducing
inflected/derived words to their word stem
base or root form
These mainly rely on chpping of 's','es','ed',
'ing','ly',
'''
import nltk
def get_steam(text):
    stemmer = nltk.porter.PorterStemmer()
    text=' '.join([stemmer.stem(word) for word in text.split()])
    return text
get_steam("We are eating and swimming; we have been eating and swimming ; he eats and swims")

###############################################
#You could write list comprehension like this:
from fnmatch import fnmatchcase
#[addr for addr in addresses if fnmatchcase(addr, '* ST')]
text1='11/27/2012'
text2='Nov 27,2012'
import re
if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')
    
if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')
    
#######################################
datepat=re.compile(r'(\d+)/(\d+)/(\d+)')
if re.match(datepat,text1):
    print('yes')
else:
    print('no')
    
if re.match(datepat,text2):
        print('yes')
else:
        print('no')
        
######################################################
#Searching and replacing text
text='yeah, but no, but yeah, but no,but yeah'
text.replace('yeah','yep')
##########################################3
text='Today is 11/27/2012. PyCon starts 3/13/2013'
import re
re.sub(r'(\d+)/(\d+)/(\d)',r'\3-\1-\2', text)


newtext, n=datepat.subn(r'\3-\1-\2',text)
newtext
n

###########################################################

text='UPPER PYTHON, Lower python, Mixed Python'
re.findall('python',text,flags=re.IGNORECASE)
#to substitute
re.sub('python','snake',text,flags=re.IGNORECASE)

#UPPER snake, lower snake,Mixed snake

##################################################
#The lasr example reveals a limitation that

import re
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


###############################################################
str_pat=re.compile(r'\"(.*)\"')
text1='Computer says "no. "'

str_pat.findall(text1)

#############################################################3
#However if we have text as below
text2='Computer says "no." Phone says "yes. "'
str_pat.findall(text2)

str_pat=re.compile(r'\"(.*?)\"')
str_pat.findall(text2)
#################################################################


comment=re.compiler(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)
import re

comment=re.compiler(r'/\*(.*?)\*/',re.DOTALL)
comment.findall(text2)

#########################################################

s1='Spicy Jalope\u00f1o'
s2='Spiy Jalopen\u0303o'
print(s1)
print(s2)
s1==s2

#######################################
import unicodedata
t1=unicodedata.normalize('NFC',s1)
t2=unicodedata.normalize('NFC',s2)
t1==t2

