class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class linkedList:
    def __init__(self):
        self.head = None
    def insertAtStart(self, value):
        if self.head == None:
            self.head = newNode
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
    def insertAtEnd(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            currentNode = self.head

x = linkedList()
x.insertAtStart(5)
