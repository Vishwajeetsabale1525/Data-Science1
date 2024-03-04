# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:11:22 2023

@author: Vishwajeet
"""
#the error signifies a situation that mostly happend duw to absense of resources
#the exception are the issue that can appear at runtime and compile error
#it majorly arises in the code or program 
#autorized by developers

#Exception handling
#exception can handle with try-except block
#handling the ZeroDivisionError Exception
a = 5  # Assigns the value 5 to variable 'a'
b = 6  # Assigns the value 6 to variable 'b'
c = a + b  # Adds 'a' and 'b' and assigns the result to variable 'c'

# Without handling exception: attempting to divide 5 by 0, which raises a ZeroDivisionError
print(5/0)

# Prints the value of variable 'c' (which is 11)
print(c)

a = 5  # Reassigns the value 5 to variable 'a' (previous assignment is overwritten)
b = 6  # Reassigns the value 6 to variable 'b' (previous assignment is overwritten)
c = a + b  # Recalculates 'c' by adding the new values of 'a' and 'b'

# Using try-except block to handle potential errors
try:
    # Attempting to perform division by zero, which will raise a ZeroDivisionError
    print(5/0)
except ZeroDivisionError:
    # If a ZeroDivisionError occurs, this block will execute, printing an error message
    print("You can't divide 5 by zero")
    # Despite the exception, the value of 'c' (11) will still be printed
    print(c)

# Handling the FileNotFoundError exception when attempting to open a non-existent file ('alice.txt')
filename = 'alice.txt'  
try:
    # Tries to open the specified file for reading
    with open(filename, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    # If the specified file is not found, this block will execute, printing an error message
    print(f"Sorry, {filename} file not found on your machine")
