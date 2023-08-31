# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 18:36:30 2023

@author: ASUS
"""

# write python program to add all the items in the list 

l1 = [1,2,3,4,5,6,7,8,9]
print(sum(l1))


def addition(l1):
    sum = 0
    for i in l1:
        sum += i
    print(sum)
    
addition(l1)
        

# write python program to multiply items in the list 

l1 = [1,2,3,4,5,6,7,8,9]

def multiplication(l1):
    mul = 1
    for i in l1:
        mul = mul * i
    print(mul)
multiplication(l1)


# write python program to get largest number in the list

l1 = [2,3,1,8,5,7,4,9]
print(max(l1))
print(min(l1))

l1 = [2,3,1,8,5,7,4,9]

def maximum_no(l1):
    x = 0
    for i in l1:
        if x < i:
            x = i
    print(x)

maximum_no(l1)


'''    
write python program to count the number of strings which satisfies the condition that the string 
length is 2 or more and first and last characters are same from  givven list of stringd given a list 
'''    
    
l1 = ['abc','xyz','aba','1221']    

def condition(l1):
    for i in l1:
        x = len(i)
        if x >= 2:
            if i[0] == i[-1]:
                print(i)
    
condition(l1)
    
    


"""
write a program to get a list sorted in increasing order by the last element of the touple 
in each touple from a given list of non-empty tuples 
"""


    
l1 = [(2,5),(1,2),(4,4),(2,3),(2,1)] 



def sorting(l1):
    l2 = []
    l3 = []
    l4 = []
    for i in l1:
        x =i[-1]
        l2.append(x)
    l2.sort()
    x = len(l2)
    for j in range(x):
        if i[-1] == l2[j]:
          l3.append(j)  

    for i in l3:
        l4.append(l1[i])
    print(l4)
sorting(l1)






















   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    























