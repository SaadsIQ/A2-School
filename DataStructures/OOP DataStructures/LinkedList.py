class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.pointer = None
        self.pointerArray = []
    def insertAtStart(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            return
        else: 
            newNode.next = self.head
            self.head = newNode
    def insertAtEnd(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            return
        currentNode = self.head
        while(currentNode.next):
            currentNode = currentNode.next
        currentNode.next = newNode
        return
    def insertAtIndex(self, value, index):
        newNode = Node(value)
        currentNode = self.head
        position = 0
        if position == index:
            self.insertAtStart(value)
            return
        else:
            while currentNode != None and position + 1 != index:
                position = position + 1
                currentNode = currentNode.next
            if currentNode != None:
                newNode.next = currentNode.next
                currentNode.next = newNode
            else:
                print("Index out of range")

    def printLL(self):
        currentNode = self.head
        while(currentNode):
            print(currentNode.value)
            currentNode = currentNode.next

llist = linkedList()
llist.insertAtStart(1)
llist.insertAtStart(2)
llist.insertAtStart(1)
llist.insertAtEnd(3)
llist.insertAtIndex(4,2)
print("Node Data")
llist.printLL()