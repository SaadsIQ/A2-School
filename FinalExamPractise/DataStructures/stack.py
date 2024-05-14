stack = [None for i in range(0,int(input("Enter stack size: ")))]
# Initialize top and base pointers, and stackFull variable
topPointer = -1 # Top pointer set to -1 to signify stack is empty
basePointer = 0
stackFull = len(stack)
item = None

def push():
    global stack, topPointer, basePointer, stackFull
    if topPointer < stackFull-1:
        # Check if stack has space
        topPointer += 1
        # Increment top pointer so it points to first index in array
        item = int(input("Enter the item: "))
        stack[topPointer] = item
        # Assign the item to the array index at topPointer
        print("item pushed to stack", item)
    else:
        print("Stack full cannot push")

def pop():
    global stack,topPointer,basePointer, stackFull
    if topPointer >= basePointer:
        # Check if there are items in the stack
        stack[topPointer] = None
        topPointer = topPointer-1
        print("Popped item: ", item)
    else:
        print("Stack is empty")

def printmethod():
    global stack
    for index in range (0,stackFull):
        print(stack[index])

numPush = int(input("Enter how many items to push to stack: "))
for _ in range(numPush):
    push()
printmethod()
numPop = int(input("Enter how many items to pop from stack: "))
for _ in range(numPop):
    pop()
printmethod()