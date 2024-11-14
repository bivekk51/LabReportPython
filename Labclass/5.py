class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Rectangle(Shape):
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
circle=Circle(5)
rectangle=Rectangle(5,8)

print("Area of circle:",circle.area())
print("Area of rectangle:",rectangle.area())