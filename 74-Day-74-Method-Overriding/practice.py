from math import pi



class Square:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x * self.y

class Circle(Square):
    def __init__(self,r):
        self.r=r
       
    def area(self):
        return pi*self.r*self.r

a=Square(23,24)
print(a.area())

b=Circle(3)
print(b.area())



