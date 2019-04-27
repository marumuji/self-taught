class Shape:
    def what_am_i(self):
        return "I am a shape"

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def calculate_perimeter(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, s):
        self.side = s
    def culculate_perimeter(self):
        return self.side * 4
    def change_size(self, s):
        self.side = self.side + s


r1 = Rectangle(5, 6)
print(r1.calculate_perimeter())
print(r1.what_am_i())

s1 = Square(4)
print(s1.culculate_perimeter())
print(s1.what_am_i())

