class Person:
    def __init__(self):
        self.name = 'Bob'


def judge(a, b):
    if a is b:
        return True
    else:
        return False

a = "a"
b = 'a'
b1 = Person()
b2 = Person()

print(judge(a, b))
print(judge(b1, b2))