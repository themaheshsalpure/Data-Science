# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:11:09 2023

@author: ASUS
"""

import json

l1 = [1,2,3,4,5,6,7,8,9]

with open('number.json','w') as f:
    json.dump(l1,f)



with open('test.json') as f:
    x = json.load(f)
    print(x)










with open('numbers.json') as n:
    x = n.read()
    print(x)
    
    
    
    
file_name = 'numbers.json'    
try :
    with open(file_name) as f:
        username = json.load(f)
except :
    username = input("Enter your name pls : ")
    with open('numbers.json') as f:
        json.dump(file_name, 'w') 
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    