class Stack:
    """

    Simple stack class that keeps track of stack elements sorted in ascending order


    """

    def __init__(self, maxSize=None):
        """
        Initialize the stack

        :param maxSize:
        """
        self.items = []
        self.maxSize = maxSize

    def push(self, item):
        """
        Add an item to the top of the stack

        :param item:
        """
        if self.maxSize is None or self.maxSize > len(self.items):
            # Add the item to the top of the stack
            self.items.append(item)
        else:
            print("Stack is full")

    def pop(self):
        """
        Removes the last item from the stack
        """
        # Check if any items there in array
        if not self.items:
            print("Stack is empty")
        else:
            # Remove the item on the top of the stack given stack is not empty
            return self.items.pop()


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.items)
print("Popping: " + str(stack.pop()))
print(stack.items)
print("Popping: " + str(stack.pop()))
print(stack.items)
print("Popping: " + str(stack.pop()))
print(stack.items)
print("Popping: " + str(stack.pop()))
