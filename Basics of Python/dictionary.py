# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:01:34 2023

@author: ASUS
"""

"""

Dictionary dont allow duplicates
dictionaries cannot have two items with the same key
"""


capitals = {'Maharashtra':'Mumbai','Gujrat':'Ahamdabad','Up':'Lakhnow','Karnataka':'Banglore'}

print(capitals)

# fetching any key value from the dictionary
capitals = {'Maharashtra':'Mumbai','Gujrat':'Ahamdabad','Up':'Lakhnow','Karnataka':'Banglore'}
print('Capital os Maharashtra is :',capitals['Maharashtra'])


# changing any entity from the dictionary
capitals = {'Maharashtra':'Mumbai','Gujrat':'Ahamdabad','Up':'Lakhnow','Karnataka':'Banglore'}
capitals['Up']='Astagaon'
print(capitals)


# Adding new entity in the dictionary
capitals = {'Maharashtra':'Mumbai','Gujrat':'Ahamdabad','Up':'Lakhnow','Karnataka':'Banglore'}
capitals['Loni']='Mirzapur'
print(capitals)


# Remove entry from the dictionary

capitals = {'Maharashtra':'Mumbai','Gujrat':'Ahamdabad','Up':'Lakhnow','Karnataka':'Banglore'}
capitals.pop('Gujrat')
print(capitals)


# delete any entity from the dictionary

capitals = {'Maharashtra':'Mumbai','Gujrat':'Ahamdabad','Up':'Lakhnow','Karnataka':'Banglore'}
del capitals['Gujrat']
print(capitals)




# Iterating through the dictionary 

capitals = {'Maharashtra': 'Mumbai', 'Gujrat': 'Ahamdabad', 'Up': 'Lakhnow', 'Karnataka': 'Banglore', 'Loni': 'Mirzapur'}

for state in capitals:
    
    print(f"The capita of {state} is {capitals[state]}")


# 📌🐍 -----------------------------------------------------------------------


capitals = {'Maharashtra': 'Mumbai', 'Gujrat': 'Ahamdabad', 'Up': 'Lakhnow', 'Karnataka': 'Banglore', 'Loni': 'Mirzapur'}

# for getting only values from the dictionary
print(capitals.values())

# for getting all the items from the dictionary 
print(capitals.items())

# for getting all the keys from the dictionary
print(capitals.keys())



# 📌🐍 -----------------------------------------------------------------------

# finding the length of the dictionary
capitals = {'Maharashtra': 'Mumbai', 'Gujrat': 'Ahamdabad', 'Up': 'Lakhnow', 'Karnataka': 'Banglore', 'Loni': 'Mirzapur'}

x = len(capitals)
print(x)



# 📌🐍 -----------------------------------------------------------------------

capitals = {'Maharashtra': 'Mumbai', 'Gujrat': 'Ahamdabad', 'Up': 'Lakhnow', 'Karnataka': 'Banglore', 'Loni': 'Mirzapur'}

print('Up' in capitals)

# 📌🐍 -----------------------------------------------------------------------

# dictionaries can have the values of the touples 

seasons = {'Summer':('Feb','Mar','April','May'),
           'Winter':('June','July','Aug','Sept'),
           'Rainy':('Oct','Nov','Dec','Jan')}

print(seasons['Rainy'])
print(seasons['Summer'][0])


# 📌🐍 -----------------------------------------------------------------------

dict2 = {'brand':'maruti','model':'creta','year':2021,'year':2021}
for x in dict2:
    print(f"{x} : {dict2[x]}")















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







