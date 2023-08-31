# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:22:45 2023

@author: ASUS
"""


# pasiing multiple arguments to the function

    
def pizza(*toppings):   
    for topping in toppings:
        print(f'You have got : {topping}')
        
        
def bill(*toppings):
    for topping in toppings:
        print(f"Your bill with extra {topping} toppings you have to pay online")
        
toppings = ('peppreoni','cheez','green peppers','mushroom')
pizza(*toppings)
    
