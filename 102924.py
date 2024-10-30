#Polymorphism
#print(len("Kiddos"))
#print(len([10,20,30]))
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,x):
        self.x = x
    @abstractmethod
    def area(self):
        return 0
    
class Square(Shape):
    def area(self):
        return self.x * self.x

sqr = Square(4)

class Circle(Shape):
    def area(self):
        return math.pi ** self.x * 2
    

class rectangle(Shape):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y
    def area(self):
        return self.x * self.y
thing = rectangle(5,7)
shapes = [Square(2),Circle(2),'fdsfdsf',rectangle(5,4)]

for shape in shapes:
    if isinstance (shape, Shape):
        print(shape.area())