class Queue:
    def __init__(self):
        self.queue = []
    def printClass(self):
        print(self.queue)
        print("Length", len(self.queue))
    def enqueue(self, value):
        self.queue.append(value)
    def deQueue(self):
        if len(self.queue) < 1:
            print("Queue is empty")
        else:
            return self.queue.pop(0)

queue = Queue()
queue.printClass()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.printClass()
queue.deQueue()
queue.deQueue()
queue.printClass()
queue.enqueue(5)
queue.printClass()
