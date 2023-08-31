# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:15:34 2023

@author: ASUS
"""


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

