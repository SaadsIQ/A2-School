class node:
    def __init__(self, theData, nextNode):
        self.data = theData
        self.next = nextNode

class LinkedList:
    def __init__(self):
        self.linkedList = [node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2), node(0,6), node(0,8), node(56,3), node(0,9), node(0,-1)]
        self.startPointer = 0
        self.emptyList = 5
            
    def output_nodes(self):
        currentPointer = self.startPointer
        while currentPointer != -1:
            print(str(self.linkedList[currentPointer].data))
            currentPointer = self.linkedList[currentPointer].next
                
    def addNode(self):
        dataToAdd = input("Enter the data to add: ")
        if self.emptyList <0 and self.emptyList > 9:
            return False
        else:
            newNode = node(int(dataToAdd), -1)
            self.linkedList[self.emptyList] = newNode
            previousPointer = 0
            currentPointer = self.startPointer
            while currentPointer!= -1:
                previousPointer = currentPointer
                currentPointer = self.linkedList[currentPointer].next
            self.linkedList[previousPointer].next = self.emptyList
            self.emptyList = self.linkedList[self.emptyList].next
        return True
myLinkedList = LinkedList()
myLinkedList.output_nodes()
myLinkedList.addNode()
myLinkedList.output_nodes()
