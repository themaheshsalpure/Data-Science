# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 19:55:13 2023

@author: ASUS
"""
# Home Assignment


# 📌🐍 -----------------------------------------------------------------------

# 1] Take 5 number in a list andd find minimum of the list and maximum of the list 

l1 = [5,8,9,3,7]
x = max(l1)
y = min(l1)
print(f"Maximum number +from the given list is : {x}") 
print(f"Minimum number of the given number is : {y}")






# 📌🐍 -----------------------------------------------------------------------


# 2] Take 5 numbers in list and make it reverse

l2 = [1,2,3,4,5]
x = l2[::-1]
print(x)








# 📌🐍 -----------------------------------------------------------------------


# 3] Take 10 numbers in a list and write a script to search for a value

l3 = [10,8,2,7,5,6,4,3,9,1]

def number(num): 
    for i in l3:
        if i == num:
            return True


num = int(input("Enter your number : "))    
x = number(num)
if x:
    print(f"{num} is present in the list")
else :
    print(f"{num} is not present in the list")
    
    
    
    
    
# 📌🐍 -----------------------------------------------------------------------    
    
    
    
# 4] Take 10 numbers in a list insert some duplicate number and write script to find duplicate 


l1 = [10,8,5,7,5,4,6,4,3,9,1]

def duplicate(l1):
    l2 = []
    for i in l1:
        if i not in l2:
            l2.append(i)
        else:
            print(f"{i} is present double in list, hence it is duplicate !")

duplicate(l1)




# 📌🐍 -----------------------------------------------------------------------


# 5] take vowels and non vowels letters and find number of vowels in the list 

l1 = ['a','b','c','d','e','f','g','h']

count = 0

for i in l1:
    if i == 'a' or i =='e' or i== 'i' or i =='o' or i =='u':
        count += 1

print(f"The number of vowels present in the list are : {count}")











