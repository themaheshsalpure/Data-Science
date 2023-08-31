# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:15:00 2023

@author: ASUS
"""


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

