class Node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode
class LinkedList:
    def __init__(self):
        self.linkedList = [Node(1,1),Node(5,4),Node(6,7),Node(7,-1),Node(2,2),Node(0,6),Node(0,8),Node(56,3),Node(0,9),Node(0,-1)]
        self.startPointer = 0
        self.emptyList = 5
    def outputNodes(self):
        currentPointer = self.startPointer
        while currentPointer != -1:
            print(str(self.linkedList[currentPointer].data))
            currentPointer = self.linkedList[currentPointer].nextNode
    def addNode(self):
        datatoAdd = (int(input("Enter the Data to add: ")))
        if self.emptyList<0 and self.emptyList>9:
            return False
        else:
            newNode = Node(int(datatoAdd),-1)
            self.linkedList[self.emptyList] = newNode
            previousPointer = 0
            currentPointer = self.startPointer
            while currentPointer != -1:
                previousPointer = currentPointer
                currentPointer = self.linkedList[currentPointer].nextNode
            self.linkedList[previousPointer].nextNode = self.emptyList
            self.emptyList = self.linkedList[self.emptyList].nextNode
        return True
    
myLinkedList = LinkedList()
myLinkedList.outputNodes()
