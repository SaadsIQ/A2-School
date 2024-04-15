arrayNodes = []
for x in range(0,20):
    arrayNodes.append([-1,-1,-1])
arrayNodes = [[1,20,5],[2,15,-1],[-1,3,3],[-1,9,4],[-1,10,-1],[-1,58,-1],[-1,-1,-1]]

def SearchValue(root, valueToFind):
    if root == -1:
        return -1
    elif arrayNodes[root][1] == valueToFind:
        return root
    elif arrayNodes[root][1] == -1:
        return -1
    if arrayNodes[root][1] > valueToFind:
        return SearchValue(arrayNodes[root][0], valueToFind)
    if arrayNodes[root][1] < valueToFind:
        return SearchValue(arrayNodes[root][2], valueToFind)
    
def postOrder(RootNode):
    if RootNode[0] !=1:
        postOrder(arrayNodes[RootNode[0]])
    if RootNode[2] !=-1:
        postOrder(arrayNodes[RootNode[2]])
    print(str(RootNode[1]))