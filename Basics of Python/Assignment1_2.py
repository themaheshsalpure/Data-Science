# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:16:10 2023

@author: ASUS
"""


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
