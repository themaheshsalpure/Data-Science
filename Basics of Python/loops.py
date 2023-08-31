# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:14:26 2023

@author: ASUS
"""


# while  loop 

count = 1
print("Starting the loop")

while count<=10:
    print(f"next number is : {count}")
    count+=1

# -----------------------------------------------------------------

# For loop 

for i in range(0,10):
    print(i)


num = int(input("Pls enter your number :"))

for i in range(0,16):
    if i == num:
        break
    
    print(i)
print("Done sir !")    


# -----------------------------------------------------------------

# Anonymous variable 

for _ in range(0,10):
    print(".", end="")



# -----------------------------------------------------------------

num = int(input("Enter your number :"))

for i in range(0,20):
    if i == num:
        continue                                # use of continue statement 
    
    print(f"my name is mahes {i} Done !")

# -----------------------------------------------------------------


# odd numbers in the perticular range
start , end = 4, 20

for i in range(start, end+1):
    if i %2 != 0:
        print(i)
        
# even number 
start , end = 4, 20

for i in range(start, end+1):
    if i %2 == 0:
        print(i)
        
# -----------------------------------------------------------------

# Adding step in loop 
for i in range(0,20,3):
    if i %2 != 0:
        print(i)

# -----------------------------------------------------------------

start = int(input("Enter your starting number :"))
end = int(input("Enter your ending number :"))

for i in range(start, end+1):
    if i %2 == 0:
        print(f"{i} is an even number !")
print("Done all even numbers ! \n")

for num in range(start, end+1):
    if num%2 != 0:
        print(f"{num} is an even number !") 
print("Done printing all the odd numbers !")


# ---------------------------------------------------------------------

# prime number 

count = 1
num = int(input("Enter your number :"))
for i in range (2,num):
    if num%i==0:
        count+=1
        
if count ==1:
    print("prime number ")
else :
    print("NOt a prime number ")


# ---------------------------------------------------------------------

# Leap year 

year = int(input("Enter your year to cheack : "))

if (year%400 == 0) and (year%100 == 0):         # TO CHEACK FOR THE CENTURY YEAR IS LEAP OR NOT
    print(f"{year} is an leap year !")
    
elif (year%4 == 0) and (year %100 != 0):        # TO CHEACK ANY OTHER YEAR IS LEAP YEAR OR NOT
    print(f"{year} is an leap year !")

else :
    print(f"{year} is not an leap year !")

# ---------------------------------------------------------------------

# is palindrome 

x = input("Enter your string :")

y = x[::-1]
print(x)

if x == y:
    print(f"{x} is an palindrome")
else :
    print(f"{x} is not an palindrome")


# -----------------------------------------------------------------------

# Mario pyramid


num = int(input("Enter height of the pyramid :"))

for i in range(num):
    h = "*"*(i+1)
    print(h.rjust(num)+" "+h)


# another logic

for i in range(4):
    for j in range(i+1):-
        print("#", end=" ")
    print()



for i in range(4):
    for j in range(4-i):
        print("#", end=" ")
    print()


# -----------------------------------------------------------------------

# function


# global variable
x = "Man"                   # this is an global variable

def info():
    print(f"Iron {x}")
    
info()


# local variable
y = "bestest"
def main():
    y = "best"         # this is an local variable it can be used only in a soecific block od code
    print(f"Python is {y}")

main()

# -----------------------------------------------------------------------

# Dictionary

x = {"name":"Mahesh","age":21}
print(x['name'])
print(x["age"])

# -----------------------------------------------------------------------

str1 = "Hello"
str2 = 2
x = str1+str2
print(x)

# -----------------------------------------------------------------------

# Multiline use 

print("""hello
      world
      my 
      name 
      is 
      mahesh""")
