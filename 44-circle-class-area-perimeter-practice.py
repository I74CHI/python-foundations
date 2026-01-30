"""PRACTICE"""
"""Q. Define a Circle class to create a circle with radius r using the constructor.
Define an Area() method of the class which calculates the area of the circle.
Define a Perimeter() method of the class which allows you to calculate the perimeter of the
circle."""

class Circle:
    def __init__(self,r):
        self.r = r
    
    def area(self):
        return (3.14)*(self.r**2)
    
    def perimeter(self):
        return 2 * (3.14) * self.r

r1 = Circle(4)
print(r1.area())
print(r1.perimeter())
