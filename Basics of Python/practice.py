# printing hello world
# print('Hello world')

#-------------------------------------------------------------

# age1 = input('Enter your age : ')
# print(age1)
#  print(type(age1))                                           # cheaking data type of the age1 -- default data type = str


# age2 = input('Enter your age :')


# age1 = int(age1)                                                # type casting of string into integer
# age2 = int(age2)                                                # type casting of string into integer

# print(age1 + age2)

# ---------------------------------------------------------------

# age = 1.5862
# x = type(age)
# print(x)

# age = int(age)                                                  # type casting floar - int
# print(age)
# print(type(age))

# age = float(age)                                                # type casting int - float
# print(age)

# ------------------------------------------------------------------

c1 = 1
c2 = 2j                                                          # complex number 

print(type(c1))
print(type(c2))

print(c1.real)
print(c2.imag)

# -------------------------------------------------------------
# Boolean

ok = True
print(type(ok))
print(ok)


age = bool(input("your name :"))

print(age)
print(type(age))

# ---------------------------------------------------------------


home = 10
away = 15

x = home + away
print(x)
print(type(x))
print(10*15)
print(type(10*15))

x = 7
y = 5

print(x-y)
print(type(x-y))


# int - int = int
print(y-x)
print(type(y-x))

x = 100
y = 20

# int/int = float
print(x/y)
print(type(x/y))

# to get output data type as int
# int//int = int
print(x//y)
print(type(x//y))

# finding remainder
print(x%y)
print(type(x%y))



# poweer operation 

a = 20
b = 5

print(a**b)




x = 1
x += 1
print(x)



winner = None
print(winner is None)


# --------------------------------------------------------------------------------------------

num = int(input("Enter your number :"))
if num > 0 :
    print(f"{num} is positive")
    
elif num == 0:
    print(f"{num} is equal to zero")
    
else :
    print(f"{num} is negative")


    

savings = float(input("Enter your savings : "))

if savings == 0:
    print("No savings, sorry sir !")
    
elif savings <500:
    print("You have good savings sir !")
    
elif savings < 1000:
    print("Your savings are best !")

elif savings < 10000:
    print("Your savings are excilent !")

else :
    print("Thank you sir !")


# -----------------------------------------------------------------

# while  loop 

count = 1
print("Starting the loop")

while count<=10:
    print(f"next number is : {count}")
    count+=1

# -----------------------------------------------------------------

# For loop 

for i in range(0,10):
    print(i)


num = int(input("Pls enter your number :"))

for i in range(0,16):
    if i == num:
        break
    
    print(i)
print("Done sir !")    


# -----------------------------------------------------------------

# Anonymous variable 

for _ in range(0,10):
    print(".", end="")



# -----------------------------------------------------------------

num = int(input("Enter your number :"))

for i in range(0,20):
    if i == num:
        continue                                # use of continue statement 
    
    print(f"my name is mahes {i} Done !")

# -----------------------------------------------------------------


# odd numbers in the perticular range
start , end = 4, 20

for i in range(start, end+1):
    if i %2 != 0:
        print(i)
        
# even number 
start , end = 4, 20

for i in range(start, end+1):
    if i %2 == 0:
        print(i)
        
# -----------------------------------------------------------------

# Adding step in loop 
for i in range(0,20,3):
    if i %2 != 0:
        print(i)

# -----------------------------------------------------------------

start = int(input("Enter your starting number :"))
end = int(input("Enter your ending number :"))

for i in range(start, end+1):
    if i %2 == 0:
        print(f"{i} is an even number !")
print("Done all even numbers ! \n")

for num in range(start, end+1):
    if num%2 != 0:
        print(f"{num} is an even number !") 
print("Done printing all the odd numbers !")


# ---------------------------------------------------------------------

# prime number 

count = 1
num = int(input("Enter your number :"))
for i in range (2,num):
    if num%i==0:
        count+=1
        
if count ==1:
    print("prime number ")
else :
    print("NOt a prime number ")


# ---------------------------------------------------------------------

# Leap year 

year = int(input("Enter your year to cheack : "))

if (year%400 == 0) and (year%100 == 0):         # TO CHEACK FOR THE CENTURY YEAR IS LEAP OR NOT
    print(f"{year} is an leap year !")
    
elif (year%4 == 0) and (year %100 != 0):        # TO CHEACK ANY OTHER YEAR IS LEAP YEAR OR NOT
    print(f"{year} is an leap year !")

else :
    print(f"{year} is not an leap year !")

# ---------------------------------------------------------------------

# is palindrome 

x = input("Enter your string :")

y = x[::-1]
print(x)

if x == y:
    print(f"{x} is an palindrome")
else :
    print(f"{x} is not an palindrome")


# -----------------------------------------------------------------------

# Mario pyramid


num = int(input("Enter height of the pyramid :"))

for i in range(num):
    h = "*"*(i+1)
    print(h.rjust(num)+" "+h)


# another logic

for i in range(4):
    for j in range(i+1):-
        print("#", end=" ")
    print()



for i in range(4):
    for j in range(4-i):
        print("#", end=" ")
    print()


# -----------------------------------------------------------------------

# function


# global variable
x = "Man"                   # this is an global variable

def info():
    print(f"Iron {x}")
    
info()


# local variable
y = "bestest"
def main():
    y = "best"         # this is an local variable it can be used only in a soecific block od code
    print(f"Python is {y}")

main()

# -----------------------------------------------------------------------

# Dictionary

x = {"name":"Mahesh","age":21}
print(x['name'])
print(x["age"])

# -----------------------------------------------------------------------

str1 = "Hello"
str2 = 2
x = str1+str2
print(x)

# -----------------------------------------------------------------------

# Multiline use 

print("""hello
      world
      my 
      name 
      is 
      mahesh""")

# -----------------------------------------------------------------------

x = "this is python"

x= x[1:7]
print(x)


# slicing from 4 to end 

x = "this is python"

x = x[4:]
print(x)


# slicing from the starting oof the string

x = "this is python"
x = x[:7]
print(x)

# -----------------------------------------------------------------------

x = "YUVRAJ"
a = x.lower()
print(a)
b = a.upper()
print(b)

# -----------------------------------------------------------------------

# replace method
x = "My name is Mahesh"
y =x.replace("Mahesh","Shubham")
print(y)

# -----------------------------------------------------------------------

# split method

x = "Hello, world"
y = x.split(',')            # this will skip the "," from hello, world 
print(y)


x = "Hello, World"
y = x.split()               # this will contain ","
print(y)


x = "hello word"

z = x.split(" ")
y = x.replace(","," ")
print(z)
print(y)

# -----------------------------------------------------------------------

x = "Hello world"
y =x[::-2]
print(y)

# -----------------------------------------------------------------------

# .find() method 

x = "Hello world"
z = x.count("l")
print(z)
y = x.find("l")
print(y)

# -----------------------------------------------------------------------

x = "Hello"
y = "World"

print(x+" "+y)

# -----------------------------------------------------------------------

# f string in python

x = "My name is"
y = "Mahesh"

print(f"Hello {x} {y}")


# ----------------------------------------------------------------------
item = 3
quantity = 5
verieties = 27

order = "I want {} item with {} quantity and with {} different verieties"

x = order.format(item,quantity,verieties)
print(x)

# -----------------------------------------------------------------------

# Escape characters 

print("Hello everyone i am from\" sanjivani college of egineering Kopargaon\"")


d = {"Name":"Mahesh","age":"21","city":"Rahata"}
print(d["Name"])


# -----------------------------------------------------------------------

# prime number using fumction

def prime_no(num):
    for i in range(2,num):
        if(num%i==0):
            print("Given number is not an Prime Number")
            break
    #print("The given number is an Prime Number")
    return 'The given number is an Prime Number'

num = int(input("Enterr your number : "))
prime_no(num)

# -----------------------------------------------------------------------

# Addition code

def add(num1,num2):
    num = num1+num2
    return num

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))

add(num1,num2)

# 📌🐍 -----------------------------------------------------------------------


def greeting():
    x = " Hello sir !"
    return x
name = input("Enter your name :")
y = greeting()
print(name+y)

# 📌🐍 -----------------------------------------------------------------------


def greet(name):
    print(f"Hello, {name} sir!")

name = input("Enter your name : ")
greet(name)

# 📌🐍 -----------------------------------------------------------------------


def pet_name(name,breed):
    print(f"I have pet named {name} and of breed {breed}")
    
pet_name('Zhural','Aditya')


def son(name='Navnath',age='20'):
    print(f"I have a son named {name} and her age is {age}")

son()


# 📌🐍 -----------------------------------------------------------------------


# Roller Coster


print("Welcome to the roller coster !")
height = int(input("Enter your height :"))
bill = 0

if height>=120:
    age = int(input("Enter your age :")) 
    if age<12 : 
        print("You have to pay Rs. 10 for you ticket !")
        bill = 10
    elif age >12 and age<18 :
        print("You have to pay Rs. 15 for you ticket !")
        bill = 15
    elif age<18 :
        print("You have to pay Rs. 20 for your ticket !")
        bill = 20
    elif age>18 :
        print("You have to pay Rs. 50 for your ticket !")
        bill = 50

        
else :
    print("You are not eligible for this ride !")
    
print("Do you waant your bill Y or N ")
x = input()

if x == 'Y':
    bill += 100000
    print(f"your bill is : {bill}")
    
else :
    print("Thank you , you didnt get bill !")


# 📌🐍 -----------------------------------------------------------------------



# create a program to find the days, weeks and month reminign to live 80 years from our birtdate 



print("Enter your birth date :")
bday = int(input("Day :"))
bmonth = int(input("Month :"))
byear = int(input("Year :"))


print("Enter current Date :")
cday = int(input("Day:"))
cmonth = int(input("Month :"))
cyear = int(input("Year :"))



def leap_year(cyear, xyear):
    count = 0
    for i in range(cyear,xyear):
        if i%4==0 and i%100 !=0:
            count+=1
    return count       
          



xyear = byear+80
#print(xyear)

remaining_year = xyear - cyear
print(f"Remaining year : {remaining_year}")

  
x = leap_year(cyear,xyear)

y = remaining_year*365
rdays = y+x
print(f"Your remining days are : {rdays}")

rmonth = x*12
print(f"Your remaining months are : {rmonth}")
 
rweeks = rdays // 7
print(f"Remaining weeks are : {rweeks}")



# 📌🐍 -----------------------------------------------------------------------


# Iteratting through the given list

users = ["Boss","Admin","Employee","Manager","Worker"]

for user in users:
    if user =='Manager':
        print(f"Hello sir, Would you like to see the condition of employees .")
    elif user =='Boss':
        print(f"Hello Sir, would you like to buy a lamborgini .")
    elif user == 'Admin':
        print(f"Hello sir, please give todays report !")
    elif user == 'Employee' :
        print(f"Hello sir, kaam kr ata pall !")
    elif user == 'Worker':
        print(f"Chal nigh ata.")
    else:
        print("Sorry !")



# 📌🐍 -----------------------------------------------------------------------

# generating an random password by using random library`


import string
import random

objectives = ["fruit","girl","boy","vehicle","colour","gender","black"]
noune = ["mango","sweet","cute","bmw","red","male","horse"]


x = random.choice(objectives)
y = random.choice(noune)

rand_number = random.randrange(1,10000)
special_char = random.choice(string.punctuation)
rand_number = str(rand_number)

print(x+rand_number+special_char+y)




# 📌🐍 ----------------------------------------------------------------------

''' write a code to cheack whether the given password is strong or weak and must folow 
following condition
1. It must be of 8 characters
2. it must have at least one upper and lower case

'''

pas = "mahesh#4334"

x = len(pas)
c = 0
d = 0
if x>=8: 
    for i in range(x): 
        a =pas[i]
        if a.islower():
            c+=1
        
        if a.isupper():
            d+=1
    
        
if c>=1 and d>=1:
    print("Your password is strong ")
else :
    print("Your password is weak")






pas = "Mahesh "
arr = []

x = len(pas)

for i in range (x):
    y = pas[i]
    print(y)
    arr.append(y)
print(arr)


# 📌🐍 -----------------------------------------------------------------------


"""
write a program to calculate the price order bill for:
    1. small - $15
    2. medium - $20
    3. laarge - $25
    
    if you want to add peproni for 

    1. small = $2
    2. medium and large = $3
    
    extra cheeze : for $1

"""

print('Welcome to the Pom-Pom pizza :')

bill = 0
x = input("which pizza would you like to order : s/m/l\n")

if x=='s':
    bill+=15
    print("Do you want peproni on it : y/n\n")
    y = input()
    if y =="y":
        bill+=2

    print("Do you want extra cheeze : y/n\n")
    z = input()
    if z=='y':
        bill+=1
        print("Extra cheeze added")


elif x=='m':
    bill+=20
    print("Do you want peproni on it : y/n\n")
    y = input()
    if y =="y":
        bill+=3

    print("Do you want extra cheeze : y/n\n")
    z = input()
    if z=='y':
        bill+=1
        print("Extra cheeze added")
        

elif x=='l':
    bill+=25
    print("Do you want peproni on it : y/n\n")
    y = input()
    if y =="y":
        bill+=3

    print("Do you want extra cheeze : y/n\n")
    z = input()
    if z=='y':
        bill+=1
        print("Extra cheeze added")
        


print(f"Your total bill is : ${bill}")
        
    
        
# 📌🐍 -----------------------------------------------------------------------
# 26- July 

def person(first,last):
    x = {'first':first, 'last':last}
    return x

y = person("ram","shinde")
print(y)

# 📌🐍 -----------------------------------------------------------------------

def users(names):
    for name in names :
        x = f"Hello, {name.title()} !"
        print(x)
        
usernames = ['mahesh','yuvraj','sanket','prafull']
users(usernames)

# 📌🐍 -----------------------------------------------------------------------

# pasiing multiple arguments to the function

def pizza(*toppings):
    print(toppings)
    
toppings = ('peppreoni','cheez')
pizza(*toppings)

    
def pizza(*toppings):   
    for topping in toppings:
        print(f'You have got : {topping}')
        
toppings = ('peppreoni','cheez','green peppers','mushroom')
pizza(*toppings)
    

    
def pizza( *args):
    # passing size and toppings from toppings it is taking f
    sizes = args[:len(args)//2]
    toppings = args[len(args)//2]
    for topping,size in zip(toppings,sizes):
        print(f'You have got : {topping} on {size} inch puzza')
        
toppings = ('peppreoni','cheez','green peppers','mushroom')
sizes = (12,13,14,15)
pizza(*sizes,*toppings)
    
    
# 📌🐍 -----------------------------------------------------------------------    
    
import pizza
pizza.pizza(*toppings)    


# importing specific funtions    
    
from pizza import bill
pizza.bill(*toppings)
    

# this will import all the functions from the module pizza    
from pizza import *
#pizza.bill(*toppings)
pizza(*toppings)        

    
# 📌🐍 -----------------------------------------------------------------------


# lmabda function - 


# this is normal function
def add(a,b,c):
    sum = a+b+c
    return sum

print(add(2,3,4))

  # this both codes are same and return same value 

# this is the lambda function
add = lambda a,b,c : a+b+c
#print(add(2,3,4))
add(2,3,4)



# multiplication using lamda funtion

# using normal function
def mul(a,b,c):
    x = a*b*c
    return x

print(mul(2,3,4))

# using lambda function

mul = lambda x,y,z : x*y*z
mul(2,3,4)



# passsing multiple arguments for function

add = lambda *args : sum(args)
add(1,2,3,4,5,6,7,8,9)


# 📌🐍 -----------------------------------------------------------------------

def person(name,**data):
    print(name)
    print(data)
    
person(name="Navin",age=19, place='Mumbai',no=9673912354)



def person(name, **data):
    print(name)
    for i,j in data.items():
        print(f"{i} : {j}")
        
person(name="Navin",age=19, place='Mumbai',no=9673912354)




val = lambda **data:sum(data.values())
val(a=1,b=2,c=3,d=4)

# if else in lambda function
# this wil give error bcz no else is given  

max = lambda x,b : a if(x>b) 
max(2,3)

# this will give proper output
max = lambda a,b : a if(a>b) else b
max(2,3)


# 📌🐍 -----------------------------------------------------------------------


# tuples 


tp1 = (1,2,3,4,5,6,7,8,9)
x = len(tp1)
for i in range(x):
    print(f"tp1[i] 7 :\t{tp1[i]}")

tp2 = (1,"mahesh",True,23.65)
print(tp2)


# iterating through touples 

fruits = ('apple','orange','plum','banana')
x = len(fruits)
for i in range(x):
    print(fruits[i])

fruits = ('apple','orange','plum','banana')
for fruit in fruits:
    print(fruit)

fruits = ('apple','orange','plum','banana')
x = fruits.count('apple')
print(x)
print(fruits.index('apple'))

fruits = ('apple','orange','plum','banana')
if "apple" in fruits:
    print("yes")
else :
    print("No")


n = (1,2,3,4,5,6,7)
x =max(n)
print(x)


# nested touples 

top1 = (1,2,3,5,5)
top2 = ('mahesh','shrikant','yuvraj')
top3 = (34.6,top1,55,67,'aditya',top2)
print(top3)



# 📌🐍 -----------------------------------------------------------------------

# list

l1 = [1,2,3,4,5]
l2 = [l1,'mahesh','yuvraj','aditya']
print(l2)

l1.append(8)
print(l1)



l1 = [1,2,3,4,5]
l1[3]=5
print(l1)
print(x1)

l1 = [1,2,3,4,5]
x = l1.pop(2)
print(x)

l1 = [1,2,3,4,5]
l1.remove(3)
print(l1)

x1=[]
l1 = [1,2,3,4,5]
x1 = l1.copy()
print(x1)

# list

l1 = [1,2,3,4,5]
l2 = [l1,'mahesh','yuvraj','aditya']
print(l2)

l1.append(8)
print(l1)



l1 = [1,2,3,4,5]
l1[3]=5
print(l1)
print(x1)

l1 = [1,2,3,4,5]
x = l1.pop(2)
print(x)

l1 = [1,2,3,4,5]
l1.remove(3)
print(l1)

x1=[]
l1 = [1,2,3,4,5]
x1 = l1.copy()
print(x1)

# list indexing and slicing

l1 = [1,2,3,4,5]
print(l1[-1])

l1 = [1,2,3,4,5]
print(l1[::-1])

l1 = [1,2,3,4,5]
l2 = [8,9]
l1.extend(l2)
print(l1)


# list concatination

l1 = [1,2,3,4,5]
l2 = [8,9]
l3 = l1+l2
print(l3)



 

