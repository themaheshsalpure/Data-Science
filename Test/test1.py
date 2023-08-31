# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:01:42 2023

@author: ASUS
"""

📌🐍-----------------------------------------------------------------------------------

# 1- 

def info(l1,l2):
    for i in l1:
        if i in l2:
            return True
        break
    return False
        
l1 = [1,2,3,4,5]
l2 = [4,6,7,89]
print(info(l1,l2))

 

📌🐍-----------------------------------------------------------------------------------



# 2 -

x = [x+6 for x in range(1,20)]
print(x)



📌🐍-----------------------------------------------------------------------------------




# 3 -
s = "Mahesh"
x = s[::-1]
print(x)



📌🐍-----------------------------------------------------------------------------------



# 4 -

d = {1:10,2:20,3:30,4:40}

for i in d:
    print(f"{i} : {d[i]}")



📌🐍-----------------------------------------------------------------------------------



# 5 -


dic = {"A":1000,"B":5000,"C":1500,"D":3000}
x = {key:values for key,values in dic.items() if values>=2000}
print(x)



📌🐍-----------------------------------------------------------------------------------



# 6 -

with open('data.txt','r') as f:
    x = f.read()
    print(x)



📌🐍-----------------------------------------------------------------------------------




# 7 -

from itertools import cycle

x = 'Hello'

for i in cycle(x):
    print(x,end=" ")


import itertools as it
start = 10
step =1
x = it.count(start, step)
for i in x:
    print(i)

📌🐍-----------------------------------------------------------------------------------



# 8 -

l = [1,2,3,4,5,6,7,8,9,10]
even = filter(lambda x:x%2==0,l)
print([i for i in even])


odd = filter(lambda x:x%2 != 0,l)
print([x for x in odd])



📌🐍-----------------------------------------------------------------------------------




# 9 - 

import pandas as pd
import numpy as np

d = {
     'name':['Anna','Dinu','Ramu','Ganu','Emily','Mahesh','Jayesh','Venkat','Ajay','Dhanesh'],
     'score':[12.5,9,16.5,np.nan, 9, 20,14.5,np.nan,8,19],
     'attempts':[1,3,2,3,2,3,1,1,2,1],
     'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes']
     }

labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(d, index = labels)
print(df)



📌🐍-----------------------------------------------------------------------------------



# 10 -

import matplotlib.pyplot as plt

l1 = [2,6,3,6,2]


x = plt.plot(l1,marker='.')

plt.show(x)





📌🐍-----------------------------------------------------------------------------------









































