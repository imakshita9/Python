'''2. Write a python program to perform the below task.
	a)Read 5 Name and Marks from user(Marks out of 100)
	b)Draw bar graph using matplotlib on marks'''

import pandas as pd
import matplotlib.pyplot as plt

for i in range (1,6):
    with open("st_data.txt","a") as s:
        name=input("Enter name of student : ")
        marks=int(input("Enter marks out of 100 : "))
        print("------------------------------------------------")
        s.write(f"{name},{marks}\n")

fn=pd.read_csv("st_data.txt", names = ['Name','Marks'])
print(fn)

fn.plot(x="Name" , y="Marks" , kind="bar")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()