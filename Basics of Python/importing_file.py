# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:17:29 2023

@author: ASUS
"""

    
# 📌🐍 -----------------------------------------------------------------------    
    
import pizza
pizza.pizza(*toppings)    


# importing specific funtions    
    
from pizza import bill
pizza.bill(*toppings)
    

# this will import all the functions from the module pizza    
from pizza import *
#pizza.bill(*toppings)
pizza(*toppings)        
