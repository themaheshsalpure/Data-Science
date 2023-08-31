# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:36:29 2023

@author: ASUS
"""


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










top1= (100,200,300)
max(top1)






