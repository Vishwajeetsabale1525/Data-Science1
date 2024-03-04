#DATE = 24/07/23

#If Statements

num = int(input('Enter Number : '))
if num>0:
    print(num)

#else
num = int(input('Enter Number : '))
if num<0:
    print("Its Negative")
else :
    print("Its Positive")
    
##############################################################    
#elif condition
    
saving = float(input("Enter the amount of Savings :"))
if saving == 0:
    print("No Saving")
elif saving < 500:
    print("Well Done")
elif saving < 1000:
    print("Thats a tidy Sum")
elif saving < 10000:
    print("Welcome Sir !")
else:
    print("Thank You !")

#############################################   
# loops 


 #While loop
count = 1
print("Starting")
while count <= 10:
    print(count)
    count += 1
    
#############################################################   
#For Loop
# loop over set of values in range
print("Print out values in range :")
for i in range(2,10):
    print(i)
    print("Done !")
    
#Break loop statement    
print('Only print code if all iterations completed')
num = int (input('Enter a number to check for :'))
for i in range(0,16):
    if i == num:
        break
    print(i)
print('Done')

################################################################
# Anonymous Variable
for _ in range(0,10):
    print('.',end='')
    print()
    
for _ in range(0,10):
    print('.',end='')
    
  
    
##############################################################  
#location of print is changes

for i in range(0,6):
    if i == num:
        break
    print(i)
    print('Done')   
    
for i in range(0,6):
    if i == num:
        break
    print(i,'',end='')
    print('Done')
    
for i in range(0,6):
    if i == num:
        break
    print(i,'',end='')
print('Done')
    
    
    
#############################################################    
#print odd numbers in given range
start,end = 4,19
for num in range(start,end+1):
    if num % 2 != 0:
        print(num,'',end ='')
 
# for even numbers
start,end = 4,19
for num in range(start,end+1):
    if num % 2 == 0:
        print(num,end =' ')
        
##########################################################
#print all even numbers in range
for num in range (2,19,2):
    if num%2 == 0:
        print(num,end=' ')
    
for num in range (1,30,6):
    if num%2 != 0:
        print(num,end=' ')

##############################################################
#code for finding  prime numbers  in given range
num=2
count=1
for i in range(count,num+1):
    if(num%count==0):
        count+=1
if(count==2):
    print("Prime Number")
else:
    print("Not a Prime Number")
    
    

    
###########################################################
start,end=1,100
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
            
def prime_num(num):
    for i in range(2,num):
        if(num%2==0):
            return "Number is Not Prime"
            break
    return "It is Prime Number"
#####################################3####################   
    
    



#leap year
year=int(input("Enter the year :"))
if(year%100==0 and year%400==0):
    print("YES Leap Year !")
elif(year%4==0 and year%100!=0):
    print("Yes Leap Year !")
else:
    print("Not A Leap Year !")
    

#is palendrome==>  

x=input("Enter number:")
y=x[::-1]
if(x==y):
    print("Is Palindrome")
else:
    print("Not a Palindrome")

start,end=0,121
for i in range(start,end+1):
    if x==x[::-1]:
        print(x)
        
#Mario Pyramid

for i in range(4):
    for j in range (4):
        print("*",end=' ')
    print()
        
    
for i in range(4):
    for j in range (i+1):
        print("*",end=' ')
    print()
    
for i in range(4):
    for j in range (4-i):
        print("*",end=' ')
    print()
 
    
for i in range(4):
    for j in range (i+1):
        print("*",end=' ')
    print()



#########################################

#global  Variable
x="awesome"
def my_function():
    print("python is "+x)
my_function()
    
#global & Local Variable   
x="awesome"
def my_function():
    x="fantastic"
    print("python is "+x)
my_function()
print("python is "+x)   
    

#######################################

#Dictionary
x={"name":"Ram","age":21}
print(type(x))
print(x)

###########################################
str1="Hello"
str2=2 
str3=str1+str2

#Multiple Strings
x="""This is Python it is very Powerful"""
print(x)

#String Slicing
print(x[2:10]) #anywhere in middle
print(x[:9]) #from start
print(x[3:])  # till end 
print(x[-15:-2])

x="prajwal bankar"
x=x.upper()
print(x)
x=x.lower()
print(x)
print(x.title())
print(x.strip())

# #find  and split function
x="Hello World"
print(x.replace("prajwal","Gallo"))
print(x.split(" "))

# to reverse given string
x="Hello World"
string1=x[::-1]
print(string1)
string1=x[::-2]
print(string1)

# to reverse given string
x="abcd efgh"
string1=x[::-1]
print(string1)
string1=x[::-2]
print(string1)

#find function
x="This is python and is very Powerful"
print(x.find("and"))

#string Concatination
x="hello"
y="world"
print(x+y)
print(x+y)
print(x+" "+y)
#############################################
#string Format
x=36
y="my name is Ram"
print(x+y) #error

x=36
y="Ram"
print(f"My age is {x} and My name is {y}")

quantity=3 
item_no=54
price=67
print(f"I want {quantity} pieces and item number is {item_no} ,and its price is {price}")

######################
my_order = "I want {} pieces and the item number is {} , its price is {}."
print(my_order.format(quantity,item_no,price))

my_order = "I want {} pieces and the item number is {} , its price is {}."
print(my_order.format(quantity,item_no,price))
######################
quantity=3 
item_no=54
price=67
my_order = "I want {0} pieces and the item number is {1} , its price is {2}."
print(my_order.format(quantity,item_no,price))

############################################
#Escape characters 
text="This is fun and it has got big\"round rido\""
print(text)

#Operator Precedance
print(3*3+3/3-3)
# PEMDAS
# paranthesis
# exponential
# 
#
#
#