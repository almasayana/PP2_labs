import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")
    def move(self, x1, y1):
        self.x = x1
        self.y = y1
    def dist(self, other_point):
         return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
    
p1 = Point(1, 2)
p1.show()
p2 = Point(2, 3)
p2.move(4, 5)
p2.show()
print("Distance between 2 points is", p1.dist(p2))