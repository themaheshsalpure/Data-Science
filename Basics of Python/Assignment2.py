# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:32:25 2023

@author: ASUS
"""

# 📌🐍 -----------------------------------------------------------------------


# write python program to add all the items in the list 

l1 = [1,2,3,4,5,6]
def sum(l1):
    sum=0
    for i in l1:
        sum = sum+i
    print(sum)

sum(l1)        



l2 = [1,2,3,4,5,6] 
print(sum(l2))   


# 📌🐍 -----------------------------------------------------------------------

# write python program to multiply items in the list 


l1 = [1,2,3,4,5,6,7,8]


def multiply(l1):
    val = 1
    for i in l1:
        val = val*i
    print(val)
    
multiply(l1)
      
      
     
        
l1 = [1,2,3,4,5,6,7,8]
mulyiply = lambda *l1 :  
print(multiply)
      
      
# 📌🐍 -----------------------------------------------------------------------
      
# write python program to get largest number in the list
l1 = [1,2,3,4,5,6,7,8]
print(max(l1))





# write python program to get smallest number from the list

l1 = [1,2,3,4,5,6,7,8]
print(min(l1))


l1 = [3,2,1,4,5,6,8,7]
l1.sort()
print(l1[0])
      
      
      
      
# write pythoon program to count the number of strings which satisfies the condition that the string 
# length is 2 or more and first and last characters are same from  givven list of stringd given a list 

l1 = ['abc','xyz','aba','1221']
count = 0

for i in l1:    
    x = len(i)
    if x >= 2:
        if i[0]==i[-1]:
            print(f"{i} : passes the criteria")
            count += 1
print(f"Number of strings pass cruteria are : {count}")            
            

# 📌🐍 -----------------------------------------------------------------------

"""
write a program to get a list sorted in increasing order by the last element of the touple 
in each touple from a given list of non-empty tuples 
"""


l1 = [(2,5),(1,2),(4,4),(2,3),(2,1)]
l2 = []
l3=[]
l4 = []

for k in l1:
    l2.append(k[-1])
l2.sort()
print(l2)
x = len(l2)    
for i in l1:
    print(i)
    for j in range(x):
        if i[-1]==l2[j]:
            l3.append(j)
for i in l3:
    l4.append(l1[i])
print(l4)



# 📌🐍 -----------------------------------------------------------------------

"""
write a program to remove duplicates from the list 
"""

l1 = [10,20,30,20,10,50,60,40,80,50,40]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)



l1 = [10,20,30,20,10,50,60,40,80,50,40]
a = set(l1)
b = list(a)
print(b)


# 📌🐍 -----------------------------------------------------------------------

"""
write a python program to copy a list
"""

l1 = [10,20,30,20,10,50,60,40,80,50,40]
l2 = l1.copy()
print(l2)

# 📌🐍 -----------------------------------------------------------------------
"""
write program to find the list of words that are longer thaan n from given list 
of words
"""

sent = 'The quick brown fox jumps over the lazy dog'
n = 3


def length(n, sent):
    l1 =[]
    x = sent.split(" ")
    for i in x:
        if len(i)>n:
            l1.append(i)
    print(l1)
length(n, sent)


# 📌🐍 -----------------------------------------------------------------------

#write python code that takes list and returns true if they have at least one common member
l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9]

a = set(l1)
b = set(l2)
y = a&b
if y != 0:
    print("True")

else :
    print("False")

print(y)



l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9]

def duplicate(l1,l2):
    for i in l1:
        if i in l2:
            return True
    return False    

duplicate(l1,l2)


# 📌🐍 -----------------------------------------------------------------------

"""
write a python program to find difference between list1 and list 2
"""
l1 = [1,3,5,7,9]
l2 = [1,2,4,6,7,8]

def difference(l1,l2):
    l3 = []
    l4 = []
    for i in l1:
        if i not in l2:
            l3.append(i)
    for j in l2:
        if j in l1:
            l4.append(j)
    print(l3+l4)
    
difference(l1, l2)  





# 📌🐍 -----------------------------------------------------------------------

"""
write a python program to convert a list of characters into a string
"""
s = ['a','b','c','d']

str1 ="".join(s)
print(str1)


# 📌🐍 -----------------------------------------------------------------------

"""
Write a python program to find the index of an item in a specified list

"""

l1 = [1,2,3,4,5,6,7,8]
print(l1.index(3))


# 📌🐍 -----------------------------------------------------------------------

"""
write python program to append one list on another list
"""
l1 = [1,2,3,4,5,6,7,8]
l2 = [9,10,11,12]

l1.extend(l2)
print(l1)




















      
      
      
      
      )