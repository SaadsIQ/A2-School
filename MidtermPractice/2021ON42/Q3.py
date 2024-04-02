ArrayNodes = [[0 for x in range(3)] for y in range(20)]
RootPointer = -1
FreeNode = 0
def AddNode(ArrayNodes,RootPointer,FreeNode):
    NodeData = int(input("Enter the data: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData<ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
        return ArrayNodes,RootPointer,FreeNode
    else:
        print("Tree is full")

def PrintAll():
    for X in range(20):
        print("{:<5} {:<5} {:<5}".format(ArrayNodes[X][0], ArrayNodes[X][1], ArrayNodes[X][2]))

for x in range(10):
   ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes,RootPointer,FreeNode)
PrintAll()

def InOrder(ArrayNodes, RootNode):
    if ArrayNodes[RootNode][0] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][0])
    print(str(ArrayNodes[RootNode][1]))  # Print the node data
    if ArrayNodes[RootNode][2] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][2])

InOrder(ArrayNodes, RootPointer)
 