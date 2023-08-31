# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:07:49 2023

@author: ASUS
"""

# list

l1 = [1,2,3,4,5]
l2 = [l1,'mahesh','yuvraj','aditya']
print(l2)

l1.append(8)
print(l1)



l1 = [1,2,3,4,5]
l1[3]=5
print(l1)


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



# remove() is used to remove a specific entity from your list
# used in specifically Web Scrapping

fruits = ['apple','orange','plum','banana']
fruits.remove('apple')
print(fruits)


# pop() function in the list 
# list.pop(index_of_the_entity_we_want_to_remove)

fruits = ['apple','orange','plum','banana']
fruits.pop(3)
print(fruits)


# inserting in the list 
fruits = ['apple','orange','plum','banana']
fruits.insert(2, 'chiku')
print(fruits)




















