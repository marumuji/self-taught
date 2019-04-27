import math

class Circle:
    def __init__(self, d):
        self.diameter = d

    def area(self):
        return math.pi * self.diameter ** 2

c1 = Circle(2)
print(c1.area())