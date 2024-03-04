# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:06:47 2023

@author: Vishwajeet
"""
#-------------------------------- -----------------#

#----------------File handing----------------------# 

#--------------------------------------------------#

with open('pi_digits.txt') as file_object:
    #the open() function need 
    #one argument: the name of the file you want to open 
    contents = file_object.read()
print(contents)
#observe the extra line at the end of output

##################################################
#rstrip() method
with open('pi_digits.txt') as file_object:
    #the open() function need 
    #one argument: the name of the file you want to open 
    contents = file_object.read()
print(contents.rstrip())

####################################
#rstrip removes the strips ,any whitespace
#right side character

#--------------------------------------
file_path = 'c:/1-python/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())

##################################
#reading line by line
filename = 'pi_digits.txt'
#we assign the name of file we're reading from to the variable  
with open(filename) as file_object:
#we assign use the with the syntax to
#let python open and close
#the file property.
    for line in file_object:
        print(line)

###################################################

#This blank lines appear because an invisible newline character
#is at the end of each line in the text file.
#using rstrip() in the each line in the print() call eliminates
#these extra blank lines occured in output
filename = 'pi_digits.txt' 
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

##########################################################
#working with a files into memory
#you can do whether you want with that data
filename= 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string =''
    for line in lines:
        pi_string += line.rstrip()
        print(pi_string)
        print(len(pi_string))

###########################################################
#writing to a file
#one of the simplest ways to save data to write it to a file.
#when you write text to a file, the output will still be 
#available after you  close the terminal contaning your programing output

filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
############################################

#appending the file
#if you want to add content to a file
#instead of writing over existing content,

#APPENDING a file --> no old data is lost(erased) , new data is added to the same
# while in WRITE --> all old data is lost and totally new data is added
filename = 'programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I also finding meaning in large dataset.\n")
    file_object.write("I love creaating apps that can run in a broweser.\n")

































































