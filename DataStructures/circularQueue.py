def enQueue():
    global arr, frontPointer, rearPointer, queueSize, queueLength
    if queueLength == queueSize:
        print("Queue full cannot enqueue:")
    else:
        if rearPointer == queueSize-1:
            rearPointer = 0
        else: 
            rearPointer += 1
        if frontPointer == -1:
            frontPointer = 0
        queueLength += 1
        item = int(input("input a number: "))
        arr[rearPointer] = item
def deQueue():
    global arr,frontPointer, rearPointer, queueLength, queueSize, item
    if queueLength == 0:
        print("Queue empty cannot dequeue")
    else:
        item = arr[frontPointer]
        arr[frontPointer] = None
        frontPointer += 1
        queueLength -= 1
        print("Item dequeued: ", item)

arr = [None for _ in range(0,int(input("Enter Queue size: ")))]
frontPointer = -1
rearPointer = -1
queueSize = len(arr)
queueLength = 0
item = None

numEnqueue = int(input("Enter the number of items to enqueue: "))
for _ in range(numEnqueue):
    enQueue()
print(arr)

numDequeue = int(input("Enter the number of items to dequeue: "))
for _ in range(numDequeue):
    deQueue()
print(arr)    

numRequeue = int(input("Enter how many items you want to push to queue: "))
for _ in range(numRequeue):
    enQueue()
print(arr)
