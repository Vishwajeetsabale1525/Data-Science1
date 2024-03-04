# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:31:47 2023

@author: Vishwajeet
"""
'''
UTF is "Unicode Transformation Format",
and '8' means 8-bit values are used in the encoding.
It is one of the most efficient and convenient encoding
formats among various encodings.
'''

string1="apple"
string2="jeei125"
string3="12345"
string4="pre@12"

string1.encode(encoding='UTF-8',errors='strict')
string2.encode(encoding='UTF-8',errors='strict')
string3.encode(encoding='UTF-8',errors='strict')
string4.encode(encoding='UTF-8',errors='strict')

text='one 🐘 and three 🐋'
print(text)
print(len(text))

'''
We encode the string into a bytes type using the
utf8 encoding and print the bytes.
we count the number of bytes in this encoding type
'''
text=text.encode('utf8')
print(text)
print(len(text))

#######################################
fname='data.txt'
with open(fname,mode='rb') as f:
    #by default it encode in utf-8
    contents=f.read()
    print(type(contents))
    print(contents)
    print(contents.decode('utf8'))
    
'''
Stripping unwanted characters from strings 
you want to strip unwanted characters, such as whitespaces
string. lstrip() and rstrip() perform stripping '''

#Whitespaces stripping
s=' hello world  \n'
s.strip()
#'hello world'
s=' hello world  \n'
s.lstrip()
#'hello world \n
s.rstrip()
s='  hello world   \n'


#Character stripping
t='---hello==='
t.lstrip('-')
t.strip('-=')


s='hello world     \n'
s=s.strip()
s


s.replace(' ','')
#'helloworld

import re
re.sub('\s+',' ',s)
'hello world'

###############################################
#Aligning the text string
text='Hello World'
text.ljust(20)
#'Hello World            '
text.rjust(20)
#'         Hello World'
text.center(20)
#'    Hello World     '

####################################################
#All of these methods accept an optional characters
text.rjust(20,'=')
#'=========Hello World'
text.center(20,'*')
#'****Hello World*****'
################################################

format(text,'>20')
#'         Hello World'
format(text,'<20')
#'Hello World         '
format(text,'^20')
#'    Hello World     '

'''
Here you can add characters to fill the as  above if 
u want to include characters
'''
format(text, '=>20s')
#'=========Hello World'
format(text, '*^20s')
#'****Hello World*****'

#This formats codes can also be used in the form of value
'{:>10s} {:>10s}'.format('Hello','World')
#'     Hello      World'

##############################################
#one benifit of format() is that it is not specific
#to string making it more general purpose.

x=1.2345
format(x,'>10')
x

format(x,'^10.2f')

######################################################
parts=['Is','Chicago','Not','Chicago?']
' '.join(parts)
'Is Chicago Not Chicago?'
','.join(parts)
'Is,Chicago,Not,Chicago?'
''.join(parts)