class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            self.stack.pop(len(self.stack)-1)
    def printClass(self):
        print(self.stack)
        print("Length", len(self.stack))

stack = Stack()
stack.printClass()
stack.push(1)
stack.push(2)
stack.push(3)
stack.printClass()
stack.pop()
stack.pop()
stack.printClass()
stack.push(5)
stack.printClass()
stack.pop()
stack.printClass()

