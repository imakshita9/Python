'''3. Write a program to maintain student information. 
For each student store studid, name, m1, m2 and m3 
(marks of 3 subjects ). 
Accept information for 2 students and display it as follows.
Student Details:
____________
Student Id: 1223
Name: Divya
M1 : 78
M2: 86
M3: 89'''

class Student_info():
    def __init__(self,studid,name,m1,m2,m3):
        self.studid= studid
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def display(self):
        print("Student information: \n")
        print("Student id = ",self.studid)
        print("Student name = ",self.name)
        print("Marks1 = ",self.m1)
        print("Marks2 = ",self.m2)
        print("Marks3 = ",self.m3)


student=[]

for i in range(1,3):
    student_id = int(input("Enter student id = "))
    name = input("Enter the name of student = ")
    marks1 = int(input("Enter marks for subject1 = "))
    marks2 = int(input("Enter marks for subject2 = "))
    marks3 = int(input("Enter marks for subject3 = "))
    print("----------------------------------------------------")

    student.append(Student_info(student_id, name , marks1, marks2, marks3))
  

for j in student:
    j.display()


