'''Write a python program to accept following details for Employee from user empid ,empname , no of certifications, Salary for e.g - 
111,Anu,20,100000
222,Shreyash,05,200000
333,saidatta,10,300000
a. store it in file emp.txt as comma separated values as shown above.  			         [08 Marks]
b. Read the data from emp.txt file and display only names whose number of Certificates are > 10.
c. Calculate Avg of salary.'''

no=int(input("Enter how many employees you want to add: "))
for i in range(1,no+1):
    with open("emp.txt","a") as e:
        empid=input("Enter the employee id: ")
        empname=input("Enter the employee name: ")
        no_cert=input("Enter the no of certifications: ")
        salary=input("Enter the salary: ")
        print("----------------------------------------------------------")
        e.write(f"{empid},{empname},{no_cert},{salary} \n")

with open("emp.txt","r") as e:
    for j in e:
        empid , empname, no_cert , salary = j.strip().split(",")
        if int(no_cert) > 10:
            print(empname)

with open("emp.txt","r") as e:
    total_salary=0
    total_emp=0

    for k in e :
        empid , empname, no_cert, salary = k.strip().split(",")
        total_emp=total_emp+1
        total_salary= total_salary + int(salary)

    avg_salary = total_salary / total_emp
    print("Average salary = ",avg_salary)
    


