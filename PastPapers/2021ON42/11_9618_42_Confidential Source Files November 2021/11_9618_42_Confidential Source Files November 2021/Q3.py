def AddNode(ArrayNode, RootPointer , FreeNode):
    NodeData = int(input("Enter the Data: "))
    if FreeNode <= 19:
        ArrayNode[FreeNode][0] = -1
        ArrayNode[FreeNode][1] = NodeData
        ArrayNode[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while not Placed:
                if NodeData < ArrayNode[CurrentNode][1]:
                    if ArrayNode[CurrentNode][0] ==-1 :
                        ArrayNode[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNode[CurrentNode][0]
                else:
                    if ArrayNode[CurrentNode][2] == -1:
                        ArrayNode[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNode[CurrentNode][2]
        FreeNode += 1
    else:
        print("Tree is full")
    return ArrayNode, RootPointer, FreeNode


    
def printAll(ArrayNode):
    for x in range(0,20):
        print(ArrayNode[x][0]," ", ArrayNode[x][1], " ", ArrayNode[x][2])
ArrayNode = [[0 for x in range (3)] for y in range (20)] #integer
RootPointer = -1 #integer
FreeNode = 0 #integer
for x in range (10):
    ArrayNode,RootPointer,FreeNode = AddNode(ArrayNode, RootPointer, FreeNode)
printAll(ArrayNode)

def inOrder(ArrayNode, RootNode):
    if ArrayNode[RootNode][0] != -1:
        inOrder(ArrayNode, ArrayNode[RootNode][0])
    print(str(ArrayNode[RootNode][1]))
    if ArrayNode[RootNode][2]!= -1:
        inOrder(ArrayNode,ArrayNode[RootNode][2])

inOrder(ArrayNode,RootPointer)