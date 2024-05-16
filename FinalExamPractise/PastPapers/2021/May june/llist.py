class node:
    def __init__(self, data, next=-1) :
        self.data = data
        self.next = next
linkedList = [node(1,1), node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
startPointer = 0
emptyList = 0
def oututNodes(linkedList,curNode):
    while curNode != -1:
        print(linkedList[curNode].data)
        curNode = linkedList[curNode].next

oututNodes(linkedList,startPointer)

def addNode(linkedList, current, emptyList):
    dataAdd=int(input("Enter data to add: "))
    if emptyList<0 and emptyList>9:
        return False
    else:
        newNode = node(int(dataAdd))
        linkedList[emptyList] = newNode
        previous = -1
        while current != -1:
            previous = current
            current = linkedList[current].next
        if previous !=-1:
            linkedList[previous].next = emptyList
        emptyList = linkedList[emptyList].next
        return True
    
print(addNode(linkedList,startPointer,emptyList))
oututNodes(linkedList,startPointer)