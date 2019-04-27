class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]
    
    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
item = stack.pop()
print('item: ', item)
print(stack.is_empty())

for i in range(0, 6):
    stack.push(i)

print('stack.peek() : ', stack.peek())
print('stack.size() : ', stack.size())

stack1 = Stack()
for c in "Hello":
    stack1.push(c)

reverse = ""
while stack1.size():
    reverse += stack1.pop()

print("reverse: ", reverse)