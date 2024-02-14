def push():
    global topPointer, item, arr, stackFull
    if topPointer < stackFull-1:
        topPointer = topPointer + 1
        item = int(input("input a number: "))
        arr[topPointer] = item

arr = [None for index in range(0,10)]
basePointer = 0
topPointer = -1
stackFull = len(arr)
item = None
print(stackFull)
numPush = int(input("Enter the number of items to push: "))
for _ in range(numPush):
    push()
numPop = int(input("Enter the number of items to push: "))
for _ in range(numPop):
    pop()