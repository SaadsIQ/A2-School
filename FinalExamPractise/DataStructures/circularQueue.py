queue = [None for _ in range (0,int(input("Enter queue size: ")))]
frontPointer = -1
rearPointer = -1
queueSize = 0
queueMax = len(queue)
item = None

def Enqueue():
    global queue, frontPointer,rearPointer,queueSize,queueMax,item
    if queueSize == queueMax:
        print("Queue full cannot enqueue")
    else:
        if rearPointer == queueMax - 1:
            rearPointer = 0
        else:
            rearPointer += 1
        if frontPointer == -1:
            frontPointer = 0
        queueSize = queueSize + 1
        item = int(input("Enter a number: "))
        queue[rearPointer] = item
def Dequeue():
    global queue, frontPointer,rearPointer,queueSize,queueMax,item
    if queueSize == 0:
        print("Queue empty cannot dequeue")
    else:
        item = queue[frontPointer]
        queue[frontPointer] = None
        frontPointer += 1
        queueSize -= 1
        print("Item dequeued: ", item)
def printQueue():
    print(queue)

printQueue()
numEnqueue = int(input("How many items to enqueue: "))
for _ in range(0,numEnqueue):
    Enqueue()
printQueue()
numdDequeue = int(input("How many items to dequeue: "))
for _ in range(0,numEnqueue):
    Dequeue()
printQueue()
