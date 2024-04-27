'''2. Write a python program to perform the below task.
	a)Read 5 Name and Marks from user(Marks out of 100)
	b)Draw bar graph using matplotlib on marks'''

import pandas as pd
import matplotlib.pyplot as plt

names=[]
Marks=[]
for i in range (1,6):
    name=input("Enter name of student : ")
    names.append(name)
    marks=int(input("Enter marks out of 100 : "))
    Marks.append(marks)
    print("------------------------------------------------")


plt.figure(figsize=(15,5))
plt.bar(names,Marks)
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()