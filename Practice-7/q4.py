''' Write a menu driven program to maintain student information. Modify Student class created in previous assignment. Add a member gpa in student class, 
add a function in student class to return GPA of a student
calculateGPA()
gpa=(1/3)*m1+(1/2)*m2+(1/4)*m3
Create an array to store Multiple students.
1. Display All Student
2. Search by id
3. Search by name
4. calculate GPA of a student
5. Exit'''


class Student_info():
    def __init__(self,student_id,name,m1,m2,m3):
        self.student_id= student_id
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def display(self):
        print("Student information: \n")
        print("Student id = ",self.student_id)
        print("Student name = ",self.name)
        print("Marks1 = ",self.m1)
        print("Marks2 = ",self.m2)
        print("Marks3 = ",self.m3)

    def calculateGPA(self):
        gpa=(1/3)*m1+(1/2)*m2+(1/4)*m3
        return gpa

student=[]

for i in range(1,3):
    student_id = int(input("Enter student id = "))
    name = input("Enter the name of student = ")
    m1 = int(input("Enter marks for subject1 = "))
    m2 = int(input("Enter marks for subject2 = "))
    m3 = int(input("Enter marks for subject3 = "))
    print("----------------------------------------------------")

    student.append(Student_info(student_id, name , m1, m2, m3))
  

ch=0
# print(student)

while ch != 5:
    print("1. Display All Student")
    print("2. Search by id")
    print("3. Search by name")
    print("4. calculate GPA of a student")
    print("5. Exit")

    ch = int(input("Enter your choice:"))

    if ch==1:
        for j in student:
            j.display()

    elif ch==2:
        id = int(input("Enter a Student ID to Search:"))
        found = 0
        for i in student:
            if i.student_id == id:
               found = 1
        
        if found == 1:
            print(f"{id} is present")
        else:
           print(f"{id} is not present")

    elif ch==3:
        name=input("Enter Student Name to Search:")
        found = 0
        for j in student:
            if j.name == name:
                found = 1

        if found == 1:
            print(f"Student {name} is present")
        else:
            print(f"Student {name} is not present")
    
    elif ch==4:
        name=input("Enter Student Name to Calculate GPA:")
        found = 0
        for j in student:
            if j.name == name:
                found = 1
                print(f"GPA:{j.calculateGPA():.2f}")

        if found == 0:
            print(f"Student {name} is not present")

    elif ch==5:
        exit()

    else:
        print("Invalid choice!")




