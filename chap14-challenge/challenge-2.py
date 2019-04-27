class Square:
    def __init__(self, s):
        self.side = s
    def __repr__(self):
        s = str(self.side) + " by " + str(self.side) + " by " + str(self.side) + " by " + str(self.side)
        return s

s1 = Square(29)
print(s1)