'''
Write a Python class named Circle constructed by a radius and two methods
which will compute the area and the perimeter of a circle.
'''
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculateCircleArea(self):
        area = (math.pi *self.radius)**2
        return area
    def calculateCirclePerimeter(self):
        perimeter = 2*math.pi*self.radius
        return perimeter

circle1 = Circle(5)
print(circle1.calculateCircleArea())
print(circle1.calculateCirclePerimeter())
