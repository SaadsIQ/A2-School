class Stack():
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            print("Stack empty")
        else:
            self.stack.pop(len(self.stack)-1)
    def printStack(self):
        print(self.stack)

stack = Stack()
stack.printStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.printStack()
stack.pop()
stack.printStack()
