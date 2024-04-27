'''Create a Person class with attributes name and age. Then, create a Student class that inherits from Person and has an additional 
attribute student_id. Implement methods to display the details of a person and a student.'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"name={self.name}  age={self.age}", end=" ")

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id

    def display(self):
        super().display()
        print(f"student id={self.student_id}")


s1= Student("isha",21,1)
s1.display()

p1= Person("shrutika",24)
p1.display()

