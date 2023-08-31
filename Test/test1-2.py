# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:07:03 2023

@author: ASUS
"""


📌🐍-------------------------------------------------------------------------------



l = [1]

c = 0
for i in l:
    if i :
        c+=1
if c>=1:
    print("Not empty")
else :
    print("Empty")
    

    
📌🐍-------------------------------------------------------------------------------    

    
    
l = [2,4,6,8]
a = [x*x for x in l]
print(a)


📌🐍-------------------------------------------------------------------------------



d = {1:10,2:20,3:30,4:40}

def check(d,k):
    x = d.keys()
    for i in x:
        if i == k:
            return "Key Exist"
            break
    return "Not exist"

a = check(d,2)
print(a)    




📌🐍-------------------------------------------------------------------------------



x = [i for i in range(100,160,10)]
print(x)
a = {i:i/100 for i in x}
print(a)




📌🐍-------------------------------------------------------------------------------


import pandas as pd
d = {
     'courses':['Data Science','artificial intelligence','cyber security','Machine learning'],
     'fees':[1000,2000,1234,3000],
     'duration':['1 month','3 moth','2 month','6 month']
     }

index = [1,2,3,4]

df = pd.DataFrame(d, index=index)
print(df)

c = ['ms','rj','sr','vj']

df.insert(3,'tutor',c)
print(df)

df.to_csv('file.csv')



📌🐍-------------------------------------------------------------------------------



def info():
    for i in range(1,10):
        yield i
        

x = info()
for i in x:
    print(i)


📌🐍-------------------------------------------------------------------------------


x = lambda x,y :[x*y]
print(x(2,3))



📌🐍-------------------------------------------------------------------------------



import numpy as np

x = np.array([0,0,0,0,0])

x = np.any(x)
print(x)
if x:
    print("Non zero element present")
else:
    print('No non zero Element present')



📌🐍-------------------------------------------------------------------------------



import matplotlib.pyplot as plt

l1 = [2,6,3,6,1]
l2 = [7,3,9,2,1]
plt.plot(l,l2, marker="+")
plt.show()



📌🐍-------------------------------------------------------------------------------



import matplotlib.pyplot as plt
lang = ['python','java','PHP','javascript','c#','c++']
popularity = [22.5,23.7,8.8,8,7.7,6.7]
plt.title('Popularity Of Language')
plt.pie(popularity, labels=lang)
plt.show()


📌🐍-------------------------------------------------------------------------------

































































    



















