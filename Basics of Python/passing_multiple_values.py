# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:16:45 2023

@author: ASUS
"""


# 📌🐍 -----------------------------------------------------------------------

# pasiing multiple arguments to the function

def pizza(*toppings):
    print(toppings)
    
toppings = ('peppreoni','cheez')
pizza(*toppings)

    
def pizza(*toppings):   
    for topping in toppings:
        print(f'You have got : {topping}')
        
toppings = ('peppreoni','cheez','green peppers','mushroom')
pizza(*toppings)
    

    
def pizza( *args):
    # passing size and toppings from toppings it is taking f
    sizes = args[:len(args)//2]
    toppings = args[len(args)//2]
    for topping,size in zip(toppings,sizes):
        print(f'You have got : {topping} on {size} inch puzza')
        
toppings = ('peppreoni','cheez','green peppers','mushroom')
sizes = (12,13,14,15)
pizza(*sizes,*toppings)
    






















