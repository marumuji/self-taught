class Horse:
    def __init__(self, n):
        self.name = n

class Rider:
    def __init__(self, n, h):
        self.name = n
        self.horse = h

oguri = Horse("Oguri")
print(oguri.name)

take = Rider("Take", oguri)
print(take.horse.name)
