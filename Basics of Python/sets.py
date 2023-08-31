# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 09:38:46 2023

@author: ASUS
"""

# creating set
"""
set doesnt allow the duplicate entities

set is represented in the {} brackets
"""

s1 = {'pranav',2,3,4,'mahesh',6,7,8}
print(s1)
print(type(s1))

s2 = s1.copy()
print(s2)

# used to add only one entity in the set

s1 = {'pranav',2,3,4,'mahesh',6,7,8}
s1.add('yuvraj')
print(s1)

# used to add more than one item in the set have to pass this values in the list to the update() method

s1 = {'pranav',2,3,4,'mahesh',6,7,8}

s1.update([10,11,12,14])
print(s1)


s1 = {1,2,3,4,5,6,7,8}
x = max(s1)
y = min(s1)
print(x)
print(y)


s1 = {'pranav',2,3,4,'mahesh',6,7,8}
s1.discard(2)
print(s1)



s1 = {1,2,3,4}
s2 = {4,5,6,1}

print('Union',s1|s2)

print('Intersectio',s1&s2)

print("Difference",s1-s2)















