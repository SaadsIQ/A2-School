def enQueue():
    global arr, frontPointer, rearPointer, queueSize, queueLength
    if queueLength == queueSize:
        print("Queue full cannot enqueue:")
    else:

        if rearPointer == queueSize:
            rearPointer = 0
        if frontPointer == -1:
            front = 0
        rearPointer += 1
        queueLength = queueLength + 1
        item = int(input("input a number: "))
        arr[rearPointer] = item

arr = [None for _ in range(0,int(input("Enter Queue size: ")))]
frontPointer = -1
rearPointer = -1
queueSize = len(arr)
queueLength = 0

numEnqueue = int(input("Enter the number of items to enqueue: "))
for _ in range(numEnqueue):
    enQueue()
print(arr)