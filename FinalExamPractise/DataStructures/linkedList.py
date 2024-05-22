class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def insertAtIndex(self, index, data):
        if index < 0:
            print("Index not valid")
            return
        newNode = Node(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        current = self.head
        currentIndex = 0
        prev = None
        while current is not None and currentIndex < index:
            prev = current
            current = current.next
            currentIndex += 1
        if currentIndex == index:
            prev.next = newNode
            newNode.next = current
        else:
            print("Out of bounds")

    def deleteNode(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            print("Key not found")
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked list contains:", elements)

llist = LinkedList()
llist.insertAtBeginning(10)
llist.insertAtEnd(100)
llist.insertAtBeginning(5)
llist.insertAtEnd(30)
llist.display()
