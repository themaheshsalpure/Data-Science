# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:24:13 2023

@author: ASUS
"""


📌🐍 -------------------------------------------------------------------------
 
string1 = 'Apple'
string2 = 'jeeil123'
string3 = '12345'
string4 = 'pre@12'

x = string1.encode(encoding='UTF8', errors='strict')
print(x)
y = string2.encode(encoding = 'UTF8', errors='strict')
print(y)
z = string3.encode(encoding='UTF8', errors='strict')
print(z)
a = string4.encode(encoding='UTF8', errors='strict')
print(a)





📌🐍 -------------------------------------------------------------------------

text = 'one 🐘 and three 🐋'

x = text.encode(encoding='UTF8', errors='strict')
print(x)



with open('data.txt',mode = 'rb') as f:
    x =f.read()
    print(x)

print(x.decode(encoding='UTF8'))


📌🐍 ------------------------------------------------------------------
'''
removing the extra spaces using strip() function

'''


x = '  hello '

z = x.strip()      # both side void space will be removed
print(z)

a = x.lstrip()      # left side void space is going to removed
print(a)

b =x.rstrip()       # right side void space is going to removed
print(b)


'''
removing any specific type of characters from string
'''
x = '-------Hello==='

a = x.lstrip('-')
print(a)

b = x.strip('-=')
print(b)



📌🐍 -------------------------------------------------------------------------
'''
replacing the space with the no space

'''

x = '     hello   world   '

a = x.replace(" ","")
print(a)




📌🐍 -------------------------------------------------------------------------

'''
removing the space 
'''

import re

x = '     Hello  world   '
y = re.sub(r'\s+', '', x)
print(y)


📌🐍 -------------------------------------------------------------------------

'''
Alligning the text 

'''

x = 'Hello World'
a = x.ljust(20, '=')
print(a)

b = x.rjust(30, '=')
print(b)

c = x.center(20, '=')
print(c)



📌🐍 -------------------------------------------------------------------------


x = 'Hello world'

a = format(x, '>20')
print(a)

b = format(x, '<20')
print(b)

c = format(x, '^20')
print(c)


d = format(x, '=>20')
print(d)

e = format(x, '*^20')
print(e)

a= '{:>10s}{:>10s}'.format('Hello', 'world')
print(a)


x = 1.2345

format(x, '^10.2f')



parts = ['is','chicago','Not','Chicago ?']
x = " ".join(parts)
print(x)


parts = ['is','chicago','Not','Chicago ?']
x = "=".join(parts)
print(x)
























































