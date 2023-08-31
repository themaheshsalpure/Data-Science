# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:17:50 2023

@author: ASUS
"""

    
# 📌🐍 -----------------------------------------------------------------------


# lmabda function - 


# this is normal function
def add(a,b,c):
    sum = a+b+c
    return sum

print(add(2,3,4))

  # this both codes are same and return same value 

# this is the lambda function
add = lambda a,b,c : a+b+c
#print(add(2,3,4))
add(2,3,4)



# multiplication using lamda funtion

# using normal function
def mul(a,b,c):
    x = a*b*c
    return x

print(mul(2,3,4))

# using lambda function

mul = lambda x,y,z : x*y*z
mul(2,3,4)



# passsing multiple arguments for function

add = lambda *args : sum(args)
add(1,2,3,4,5,6,7,8,9)


# 📌🐍 -----------------------------------------------------------------------

def person(name,**data):
    print(name)
    print(data)
    
person(name="Navin",age=19, place='Mumbai',no=9673912354)



def person(name, **data):
    print(name)
    for i,j in data.items():
        print(f"{i} : {j}")
        
person(name="Navin",age=19, place='Mumbai',no=9673912354)




val = lambda **data:sum(data.values())
val(a=1,b=2,c=3,d=4)

# if else in lambda function
# this wil give error bcz no else is given  

max = lambda x,b : a if(x>b) 
max(2,3)

# this will give proper output
max = lambda a,b : a if(a>b) else b
max(2,3)

