class node:
    def __init__(self, theData, nextNode):
        self.data = theData
        self.next = nextNode

class LinkedList:
    def __init__(self):
        self.linkedList = [node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2), node(0,6), node(0,8), node(56,3), node(0,9), node(0,-1)]
        self.startPointer = 0
        self.emptyList = 5
    def output_nodes(self, currentPointer):
        while currentPointer != -1:
            print(str(self.linkedList[currentPointer].data))
            currentPointer = self.linkedList[currentPointer].next
myLinkedList = LinkedList()
myLinkedList.output_nodes(0)