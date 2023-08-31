# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:13:28 2023

@author: ASUS
"""

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
