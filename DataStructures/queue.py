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

arr = [None for index in range(0,int(input("Enter Queue size: ")))]
frontPointer = 0
rearPointer = -1
queueSize = len(arr)
queueLength = 0
item = None

numEnqueue = int(input("Enter the number of items to enqueue: "))
for _ in range(numEnqueue):
    enQueue()
#numDequeue = int(input("Enter the number of items to dequeue: "))
#for _ in range(numdeQueue):
#    deQueue()
print(arr)