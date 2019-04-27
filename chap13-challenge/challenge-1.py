class  Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def calculate_perimeter(self):
        return self.width * self.height

class Square:
    def __init__(self, s):
        self.side = s
    def culculate_perimeter(self):
        return self.side * 4
    def change_size(self, s):
        self.side = self.side + s


r1 = Rectangle(5, 6)
print(r1.calculate_perimeter())

s1 = Square(4)
print(s1.culculate_perimeter())

s1.change_size(-3)
print(s1.side)