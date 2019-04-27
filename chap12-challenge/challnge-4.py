class Hexagon:
    def __init__(self, sl):
        self.sideLength = sl 

    def calculate_perimeter(self):
        return self.sideLength * 6

h1 = Hexagon(5)
print(h1.calculate_perimeter())

