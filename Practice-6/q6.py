'''Write a python program to read below data from file and find the total salary.
Data:
Anubhav|20000
Rajat|30000
Neha|50000
(Note: Put the data in .txt and then read by code)'''

with open("salary.txt","w") as s:
    s.write("Anubhav|20000\n")
    s.write("Rajat|30000\n")
    s.write("Neha|50000\n")

with open("salary.txt","r") as s:
    total_salary=0
    for i in s:
        name,salary=i.strip().split("|")
        total_salary=total_salary+int(salary)

    print("Total salary= ",total_salary)
        