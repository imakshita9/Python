'''Write a python program to accept multiple strings and numbers in any sequence from user and store it in the list. Ask user do you want to see strings or number.
If strings then navigate through the list and display only strings from the list  otherwise display only numbers from the list.'''

import re

list_input=[]

list_input=input("Enter the string = ").split()
print(list_input)

print("1. Print numbers :\n 2. Print String :")

choice = int(input("Enter your choice : "))

if choice == 1:
    for i in list_input:
        if re.match(r'^\d+$',i):
            print(i)

if choice == 2:
    for j in list_input:
        if re.match(r'^[a-zA-Z]+$',j):
            print(j)
