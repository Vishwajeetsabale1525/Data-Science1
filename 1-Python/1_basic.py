#DATE = 21/07/23

print("Hello ")

x=1
print(x)
print(type(x))
x= "a"
print(x)
print(type(x))


age = input("Please enter your age :")
print(type(age))
print(age)

################################################
#Typecasting

age1 = int(input("Please enter your age1 :"))
print(type(age1))
print(age1)

age2 = int(input("Please enter your age2 :"))
print(type(age2))
print(age2)

age = age1+age2
print(age)

#######################################################
#Floating point number
exchange_rate = 1.83
print(exchange_rate)
print(type(exchange_rate))


#########################################################
#conversion--> to Floats

int_value = 100
string_value ='1.5'
float_value = float(int_value)
print('int value as a float :',float_value)
print(type(float_value))
float_value = float(string_value)
print('string value as a float :',float_value)
print(type(float_value))

##########################################################
# Comlpex Number
c1 = 1
c2 = 2j
print('c1:',c1,', c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

######################################################
#Boolean Values

all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))

######################################################
#String --> Boolean

status = bool(input('OK it is Confirmed? :'))
print(status)
print(type(status))

#####################################################
#Arithematic Oparations

# Addition
home = 10
away = 15
print(home + away)
print(type(home + away))
print(10*4)
print(type(10*4))

# Substarct
goals_for = 10
goals_against=7
print(goals_for - goals_against)
print(type(goals_for - goals_against))

#Division
print(100/20)
print(type(100/20))

print(100//20)
print(type(100//20))

#Modulas
print('Remainder of division is :',100 % 13)
print(3%2)

#Power
a=2
b=3
print(a**b)


#####################################################
# Assignment Operators

# Compound Operatore --> (  +- )
x=0
print(x)
x += 2
print(x)


# NONE Value
winner = None
print(winner is None)
print(winner is not None)

winner = None
print('winner :',winner)
print('winner is None :',winner is None)
print('winner is not None :',winner is not None)
print(type(winner))
print('Set winner to True')
winner = True

#####################################################