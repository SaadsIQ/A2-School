queue = [None for _ in range(0,int(input("Enter queue size: ")))]
print(queue)
frontPointer = 0
rearPointer = -1 # Set to -1 to indicate empty queue
queuesize = len(queue)
queueLength = 0
item = None

def enqueue():
    global queue,frontPointer,rearPointer,queuesize,queueLength
    if queueLength == queuesize:
        print("Queue full cannot enqeue")
    else:
        queueLength += 1
        rearPointer += 1
        item = int(input("Enter a item: "))
        queue[rearPointer] = item # Item added to position of the rear pointer// back of queue
        print("Item enqueued: ", item)
def dequeue():
    global queue,frontPointer,rearPointer,queuesize,queueLength
    if queueLength == 0:
       print("Queue empty cannot dequeue")
    else:
        item = queue[frontPointer] # Item set to the item stored at front of queue
        queue[frontPointer] = None # Front of queue set to None
        frontPointer += 1 # Front pointer incremented to point to next item 
        queueLength -= 1 # Queue length decremented to show a item has been removed
        queue[:] = queue[frontPointer:] # Items from the index of frontpointer and onwards are moved to the beginning of the queue
        frontPointer = 0 # frontPointer reset as after moving the data to the beginning of the queue the next item to be dequeued will be at index 0
        print("Item dequeued: ",item)

numEnqueue = int(input("Enter the number of items to enqueue: "))
for _ in range(0,numEnqueue):
    enqueue()
print(queue)
numDequeue = int(input("Enter the number of items to Dequeue: "))
for _ in range(0,numDequeue):
    dequeue()
print(queue)
