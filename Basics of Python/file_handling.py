# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:21:55 2023

@author: ASUS
"""


# 📌🐍 -----------------------------------------------------------------------

# used to open any file and read and print the content of that file

with open('pi_digits.txt') as file:      # this will open the file given
    content = file.read()                # will reaad the content from the opened file 
    print(content)
    
    

with open('pi_digits.txt') as file:      # .open() will open the file given
    content = file.read()                # file.read() will read the content from the opened file 
    print(content.rstrip())
    
    # .rstrip() i used to remove the space printed after the content of the file
    
    
    
    
    
  
# 📌🐍 -----------------------------------------------------------------------    

# relaative path just file name 
# absolute path is complete address of the file from the dictionary 


# using back slash

file_path = 'C:\\1-python\\pi_digits.txt'
with open(file_path) as file :
    content = file.read()
    print(content)

    
# using front slash

file_path = 'C:/1-python/pi_digits.txt'
with open(file_path) as file :
    content = file.read()
    print(content)

# 📌🐍 -----------------------------------------------------------------------    

# code will read the file line by line but there will be space after every line 
with open('pi_digits.txt') as file:
    for line in file:
        print(line)



# the space between the readed lines will be removed by using .rstrip() function
with open('pi_digits.txt') as file:
    for line in file:
        print(line.rstrip())




file_name = 'pi_digits.txt'
with open(file_name) as file:
    lines = file.readline()
    string = ' '
    for line in lines:
        string += line.rstrip()
        print(string)
        print(len(string))



# writing to the file

with open('programming.txt','w') as file:
    file.write(" Mahesh Salpure ")
    
with open('programming.txt') as file1:
    for line in file1:
        print(line)


with open('programming.txt','w') as file:
    file.write("My name is Mahesh ")
    file.write('\n Hello ')



# appending an file



with open('programming.txt','a') as file:
    file.write("\n Hii sir !")

































