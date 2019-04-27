class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h

    def area(self):
        return self.bottom * self.height / 2

t1 = Triangle(3, 4)
print(t1.area())