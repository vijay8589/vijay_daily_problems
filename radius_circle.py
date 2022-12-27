"""Write a Python program which accepts the radius of a circle from the user and compute the area. 
Sample Output :
r = 1.1
Area = 3.8013271108436504"""

from math import pi
r = 1.1
area_circle = pi*r**2
print(area_circle)



class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())

