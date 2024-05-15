class Queue:
    def __init__(self):
        self.queue = []
    def printQueue(self):
        print(self.queue)
    def Enqueue(self,value):
        self.queue.append(value)
    def Dequeue(self):
        if len(self.queue) <1:
            print("Queue is empty")
        else:

            return self.queue.pop(0)
        
queue = Queue()
queue.printQueue()
queue.Enqueue(1)
queue.Enqueue(2)
queue.Enqueue(3)
queue.printQueue()
queue.Dequeue()
queue.printQueue()
