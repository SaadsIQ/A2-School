def enQueue():
    global queueLength, queueLength, rearPointer, arr#
    if queueLength == queueSize:
        print("Queue full cannot enqueue")
    else:
        queueLength = queueLength + 1
        rearPointer = rearPointer + 1
        item = int(input("input a number: "))
        arr[rearPointer] = item
        print("Item enqueued: ", item)

def deQueue():
    global arr, frontPointer, rearPointer, queueLength, queueSize, item
    if queueLength == 0:
        print("Queue full cannot dequeue")
    else:
        item = arr[frontPointer]
        arr[frontPointer] = None
        frontPointer += 1
        queueLength -= 1
        print("Item dequeued: ", item)
        for index in range(0, queueLength):
            arr[index], arr[index+1] = arr[index+1], arr[index]
            index = index + 1


arr = [None for index in range(0,int(input("Enter Queue size: ")))]
frontPointer = 0
rearPointer = -1
queueSize = len(arr)
queueLength = 0
item = None

numEnqueue = int(input("Enter the number of items to enqueue: "))
for _ in range(numEnqueue):
    enQueue()
numDequeue = int(input("Enter the number of items to dequeue: "))
for _ in range(numDequeue):
    deQueue()
print(arr)