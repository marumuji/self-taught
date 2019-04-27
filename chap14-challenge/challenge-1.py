class Square:
    square_list = []
    def __init__(self, s):
        self.side = s
        self.square_list.append(self)

s1 = Square(10)
s2 = Square(20)
print(Square.square_list)