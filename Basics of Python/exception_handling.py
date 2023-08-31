# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:17:41 2023

@author: ASUS
"""


# 📌🐍 -----------------------------------------------------------------------    

try:
    print(5/0)
except error:
    print("cant devide 5 by 0")
    
    
# 📌🐍 -----------------------------------------------------------------------    

a = 5
b = 5
c = a+b

try :
    print(5/0)
except Exception as e:
    print('Cant devide 5 by 0, chyamaila dusra input de...!')
    
    
    
# 📌🐍 -----------------------------------------------------------------------    


try :
    with open('mahesh.txt',encoding = 'utf-8') as file:
        content = file.read()
        print(content)
        
except FileNotFoundError:
    print("Wrong file name ")        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        