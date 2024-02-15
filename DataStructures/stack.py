def push():
    global topPointer, item, arr, stackFull
    if topPointer < stackFull-1:
        topPointer = topPointer + 1
        item = int(input("input a number: "))
        arr[topPointer] = item
        print("Item pushed: ", item)
    else: 
        print("Stack full cannot push")

def pop():
    global topPointer, basePointer,item, stackFull
    if topPointer >= basePointer: #IF there are items in the array
        arr[topPointer] = None
        topPointer -= 1
        print("Popped item: ", item)
    elif topPointer == basePointer-1: #IF stack empty
        print("Stack empty")

arr = [None for index in range(0,int(input("Enter stack size: ")))]
basePointer = 0
topPointer = -1
stackFull = len(arr)
item = None

numPush = int(input("Enter the number of items to push: "))
for _ in range(numPush):
    push()
numPop = int(input("Enter the number of items to pop: "))
for _ in range(numPop):
    pop()

print(arr)