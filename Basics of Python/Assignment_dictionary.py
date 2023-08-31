# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:44:31 2023

@author: ASUS
"""

# write a python prgram to add key to a dictionary
# sample d = {0:10,1:20}

-
`
a.update({2:30})
print(a)


# write python script to concatenate the following dictionary to create a new one

dic1 = {1:10,2:20}
dic2 = {3:30,4:40}
dic3 = {5:50,6:60}
dic4 = {}

for i in (dic1,dic2,dic3):
    dic4.update(i)
print(dic4)


# write a python program to cheak whther a given key is present in dictionary or not

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
y = int(input("Enter your key : "))


def check(y,d):
    x = d.keys()
    l1 = []
    l1.append(x)
    for x in d:
        if y in x:
            return "Already present !"
        else :
            return "Not present !"
        
x = check(y,d)
print(x)
        
        


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
y = int(input("Enter your key : "))

def check():
    k = d.keys()
    for i == k:
        if y == i:
            return True
        
        
        
        
        
        
        
#________________________________________________________________
#The JSON (Javascript Object Notation) format was originally developed for JS
#using json.dump() and json.load()


import json
numbers=[2,3,5,7,11,13]
filename='numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)


#________________________________________________________________
# saving your data with json is useful 
#when working with user generated data


import json
username=input("What is your name?")
filename='username.json'
with open(filename,'w') as f:
    json.dump(username,f)
print(f"We'll remember you when you come back,{username}!!!")


#________________________________________________________________



import json
filename='username.json'
with open(filename) as f :
        username =json.load(f)
print(f"Welcome back,{username}!!!")


#________________________________________________________________

#LOad the username, if it has been stored previously
# Otherwise, prompt for the username and store it



filename='username.json'
try:
    with open(filename) as f:
        username =json.load(f)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename,'w') as f:
        json.dump(username,f)
        print(f"We'll remember you when you come back,{username}!!")

else:
    print(f"Welcome back,{username}!!!")        
        
        
        
    /