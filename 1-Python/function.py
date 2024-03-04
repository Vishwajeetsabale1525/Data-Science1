#FUNCTIONS ==>
# function name only in small letters
# and no space in between

def prime_num(num):
    for i in range(2,num):
        if(num%i==0):
            return "NOT Prime"
            break
    return "Is Prime"
x=int(input("Enter num :"))
print(prime_num(x))

##################################
#function without argument
def greet_user():
#"""Display a simple Greeting."""
    print("Hello!")
greet_user()
#########################################
#Passing Information to a function
def greet_user(username):
    print(f"Hello, {username} !")
greet_user("Sanjivani AI")

#########################################
#Arguments and Parameters

def describe_pet(animal_type,pet_name):  #---->positional arguments:
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
describe_pet("Dog","Moti")
#order maters of dog and moti 

def describe_pet(animal_type="Dog",pet_name="Moti"):  #---->positional arguments:
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
describe_pet()

def describe_pet(animal_type,pet_name="Kittu"):  #---->positional arguments:
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type="Dog")

############################################
#Avoiding Argument Errors
def describe_pet(animal_type,pet_name):  #---->positional arguments:
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet()

########################################################
# Assignment 1:
    
def days_left(age):
    age_left=80-age
    days=365*age_left
    weeks=52*age_left
    months=12*age_left
    return f"You have {days} days, {weeks} weeks, {months} months remained"
age=int(input("Enter your age"))
print(days_left(age))

#code 2
from datetime import datetime
def calculate_remaining_time(birth_date):
    current_date = datetime.now().date()
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    target_date = birth_date.replace(year=birth_date.year + 80)
    remaining_time = target_date - current_date
    days_left = remaining_time.days
    weeks_left = days_left // 7
    months_left = days_left // 30
    return days_left, weeks_left, months_left
if _name_ == "_main_":
    birth_date_input = input("Enter your birth date in the format YYYY-MM-DD: ")
    try:
        days_left, weeks_left, months_left = calculate_remaining_time(birth_date_input)
        print("You have approximately:")
        print(f"{days_left} days left until you turn 80.")
        print(f"{weeks_left} weeks left until you turn 80.")
        print(f"{months_left} months left until you turn 80.")
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")


# Assignment 2:

#write a program for roller coaster if your hight is greter than 120cm
#  then eligible to play roller coaster
# 1)if your age is under 18 the tiket will be 20rs If your age is greter than 18 year then tikit tikit will be Rs50
# 2)if your age is 12 year and hight is 120cm then tikit is Rs10
# 3)if your age is between 12 to 18 then the tikit is Rs15
print("Welcome tp roller coaster")
height=int(input("Enter a height: "))
bill=0
if height>=120:
    print("U are eligible to play rolar coastar")
    age=int(input("Enter your age:"))
    if age<12:
        print("Your bill is Rs 5 Rs")
        bill=5
    elif age<=18:
        print("Your bill is Rs 10")
        bill=10
    else:
        print("Your bill is Rs 15")
        bill=15
    want_photo=input("Do you want photo Y or N : ")
    if want_photo=='Y':
        bill+=3
        print(f"Your bill is Rs {bill}.")
    else:
        print(f"Your bill is Rs {bill}.")
     
else:
    print("NOT Eligible !")
    
#############################################################
#
users=["admin","employee","manager","worker","staff"]
for user in users:
    if user=="admin":
        print("hello admin,would you like to see a status report?")
    elif user=="employee":
        print("Hello employee")
    elif user=="manager":
        print("Hello manager")
    elif user=="worker":
        print("Hello worker")
    else:
        print("Hello")


##########################################################################
import string
#Pick adjectives
adjectives=['sleepy','slow','smelly','wet','fat','red','orange','yellow','green']
#pick nouns
nouns=['apple','dinosaur','ball','toaster','goat','dragon','hammer','duck','panda']
#pick the words
import random
adjectives=random.choice(adjectives)
nouns=random.choice(nouns)
#Select number
number = random.randrange(0,100)
#select special character
special_char = random.choice(string.punctuation)
#create new secure password
password = adjectives + nouns + str(number) + special_char
print('Your new password is: %s' % password)



####################################################################
print("Welcome to Password Picker")
while True:
    adjectives=random.choice(adjectives)
    nouns=random.choice(nouns)
    #Select number
    number = random.randrange(0,100)
    #select special character
    special_char = random.choice(string.punctuation)
    #create new secure password
    password = adjectives + nouns + special_char + str(number)
    print('Your new password is: %s' % password)
    response=input('Would you like to generate another password ?\nType Y or N :')
    if response=='N':
        break

###################################################################
#write python code that determine whether or not
#a password strong.we define strong password if it follow 
#following condition
#1.it must have at least 8 character 
#atleast one upper case letter 
#atleast one lower case letter
def checkPassword(password):
    has_upper= False
    has_lower= False
    has_num= False
#check each character in password and see which meets requirements
    for ch in password:
        if ch>="A" and ch<="Z":
            has_upper=True
        elif ch>="a" and ch<="z":
            has_lower=True
        elif ch>="0" and ch<="9":
            has_num=True
    if len(password)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False

p=input("Enter a Password :")
if checkPassword(p):
    print("Strong Password")
else:
    print("Weak Password")

##########################################################
#age counting
print("What is your todays age")
years_today=input("years :")
months_today=input(" months :")
days_today=input(" days :")
total_days_today=int(years_today)*365+int(months_today)*30+int(days_today)
print(f"your total age today in days {total_days_today}")
print("Let us assume you are expected to live 90 years")
total_days_to_live=90*365
remaining_days_to_live=total_days_to_live-total_days_today
print(f"your remaining life in days {remaining_days_to_live}")


#Write a program to cal pizza order
#bill 
#is small pizze 15$
#medium 20
#Large 25$
#to add paperony on small +2$
#paperony on meduim or large +3
#for extra cheeze on any size +1$

print("welcome to the pizza hut")
size_pizza=input("Please enter the size of pizza ,S,M,L:")
add_pepp=input("do you want pepprani?Y or N: ")
extra_cheese=input("Do you want extra cheese,Y or N: ")
bill=0
if size_pizza=='S':
    print("prise is 15$")
    peprani=input('you can add peprani ')
    bill=15
if size_pizza=='M':
    print("You need to pay 20$")
    bill=20
elif size_pizza=='L':
    print("You need to pay 25$")
    bill=25

if add_pepp=='Y':
    if size_pizza=='S':
        bill+=2
    else:
        print('bill')
if add_pepp=='Y':
    if size_pizza=='M':
        bill+=3
    else:
        print('bill')
if add_pepp=='Y':
    if size_pizza=='L':
        bill+=3
    else:
        print('bill')
  
#####################################################
print("Welcome to Pizza Hut")
size = input("Please enter size of pizza --> S,M,L :")
bill=0
if size=='S':
    bill=15
    pepperoni=input("Do you want pepperoni on pizza Y or N : ")
    if pepperoni=='Y':
        bill+=2
        extra_cheese=input("Do you want extra cheese Y or N :")
        if extra_cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} $.")
        else:
            print(f"Your bill of pizza is {bill} $.")
    elif pepperoni=='N':
        extra_cheese=input("Do you want extra cheese Y or N :")
        if extra_cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} $.")
        else:
            print(f"Your bill of pizza is {bill} $.")
            
elif size=='M':
    bill=20
    pepperoni=input("Do you want pepperoni on pizza T or N : ")
    if pepperoni=='Y':
        bill+=3
        extra_cheese=input("Do you want extra cheese Y or N :")
        if extra_cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} $.")
        else:
            print(f"Your bill of pizza is {bill} $.")
    elif pepperoni=='N':
        extra_cheese=input("Do you want extra cheese Y or N :")
        if extra_cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} $.")
        else:
            print(f"Your bill of pizza is {bill} $.")
elif size=='L':
    bill=25
    pepperoni=input("Do you want pepperoni on pizza T or N : ")
    if pepperoni=='Y':
        bill+=3
        extra_cheese=input("Do you want extra cheese Y or N :")
        if extra_cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} $.")
        else:
            print(f"Your bill of pizza is {bill} $.")
    elif pepperoni=='N':
        extra_cheese=input("Do you want extra cheese Y or N :")
        if extra_cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} $.")
        else:
            print(f"Your bill of pizza is {bill} $.")
else:
    print(f"Your bill of pizza is {bill} $.")

#-------------------------------- -----------------#

#--------------------------------------------------# 

#--------------------------------------------------#
#returning a dictionary
def build_person(first_name, last_name):
#return a dictionary of info about a person."""    
    person = {'first': first_name, 'last':last_name}
    return person
musician=build_person('ram','sarkar')
print(musician)

#######################################################

#passing a list
def greet_user(names):
    for name in names:
        msg=f"Hello,{name.title()}!"
        print(msg)
username = ['Prajwal','Abhi','Sahil','Aniket']
greet_user(username)

#######################################################
#passing an arbitary number of arguments
def make_pizza(*toppings):
    print(toppings)
make_pizza=('Peprani')
make_pizza=('mashroom','green_papers','extra chess')

#####################
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza('Peprani')
make_pizza('mashroom','green_papers','extra chess')

###################################
#mixing positional and arbitary argument 
def make_pizza(size, *toppings):
    print(f"\nMaking a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,'Peprani')
make_pizza(12,'mashroom','green_papers','extra chess')

#########################################################
import pizza 

pizza.make_pizza(16,'Peprani')
pizza.make_pizza(12,'mashroom','green_papers','extra chess')

########################################################
#importing spacific function
from pizza import make_pizza
make_pizza(16,'Peprani')
make_pizza(12,'mashroom','green_papers','extra chess')

########################################################

#using as to give a functions as alias
from pizza import make_pizza as mp 
make_pizza(16,'Peprani')
make_pizza(12,'mashroom','green_papers','extra chess')

#########################################################
#Using as to give a module as alias
import pizza as p
p.make_pizza(16,'Peprani')
p.make_pizza(12,'mashroom','green_papers','extra chess')

########################################################
#importing all function in the module
from pizza import*
make_pizza(16,'Peprani')
make_pizza(12,'mashroom','green_papers','extra chess')

######################################################
#scope of variable
x=x+1
x=6
print(x)

#you cannot refrence a variable
#until it has binn assign the value
#correct
x=6 #1st initialise the variable
x=x+1 
print(x)

###################################
#lambda function or anonameous function
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))
add=lambda a,b,c:a+b+c
add(4,5,6)

################################################
def mul(a,b,c):
    mul=a*b*c
    return sum
print(mul(4,5,6))
mul=lambda a,b,c:a*b*c
mul(4,5,6)

###############################################
val=lambda *args:sum(args)
val(1,2,3,5,6)
val(1,2,3,5,7,8,9)
 
##################################################
#*args
person('navin',28,'Mumbai',98576)
###################
def person(name,**data):
    print(name)
    print(data)
    
person(name='Navin',age=28,place='Mumbai',mob_no=985060)

######################################################
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
        
person(name='Navin',age=28,place='Mumbai',mob_no=985060)

############################################################
val = lambda **data:sum(data.values())
val(a=2,b=6,c=7,d=10)

#########################################################
max=lambda a,b:x if(a>b)
print(max(1,2))

max=lambda a,b:x if(a>b) else b
print(max(1,2))
print(max(8,10))

