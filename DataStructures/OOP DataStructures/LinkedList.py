class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
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
    def insertAtIndex(self, value):
    def printLL(self):
        currentNode = self.head
        while(currentNode):
            print(currentNode.value)
            currentNode = currentNode.next

llist = linkedList()
llist.insertAtStart(1)
llist.insertAtStart(2)
llist.insertAtStart(1)
llist.insertAtEnd(2)

print("Node Data")
llist.printLL()