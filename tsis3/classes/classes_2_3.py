class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
    
s1 = Square(15)
print("Area of Square:", s1.area())  
     
r1 = Rectangle(4, 2)
print("The area of rectangle is:", r1.area())
