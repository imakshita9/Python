'''Create a Shape class with a method area that returns 0. Then, create a Rectangle class that inherits from Shape and overrides the area method 
to calculate and return the area of a rectangle. Create a Circle class that also inherits from Shape and overrides the area method to calculate and 
return the area of a circle.'''

class Shape:

    def area():
        return 0
    
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        area = self.length * self.breadth
        return area
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        area = 3.14 * self.radius * self.radius 
        return area
    

r1= Rectangle(12,10)
print("Area of rectangle = ",r1.area())

c1= Circle(4)
print("Area of circle = ",c1.area())

radius = float(input("Enter radius of circle : "))
c2= Circle(radius)
print("Area of circle = ",c2.area())
