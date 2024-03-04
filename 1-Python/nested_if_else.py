'''
Write python code using nested if else.so as to check height as well as
so as to allow for roller coster
@author: Vishwajeet
'''

print("Welcome to the roller coaster")
height=int(input("Please enter your height"))
age=int(input("Please enter your age "))
if height>=120:
    print("you can ride the roller coaster")
    if age<=18:
        print("your ticket will be 7$")
    else:
        print("your ticket will be 12$")
else:
    print("Sorry,you need to grow taller before you can ride")    