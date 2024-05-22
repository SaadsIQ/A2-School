QueueArray = ["" for i in range(10)] #ARRAY 10 ELEMENTS STRING
headPointer = 0 #INTEGER
tailPointer = 0 #INTEGER
numberOfItems = 0 #INTEGER

def Enqueue(QueueArray, headPointer,tailPointer,numberOfItems,DataToAdd):
    if numberOfItems == 10:
        return False
    QueueArray[tailPointer] = DataToAdd
    if tailPointer >=9:
        tailPointer = 0
    else:
        tailPointer = tailPointer +1
    numberOfItems += 1
    return True,QueueArray,headPointer,tailPointer,numberOfItems

def Dequeue(QueueArray,headPointer,tailPointer,numberOfItems):
    if numberOfItems == 0:
        return False,QueueArray,headPointer,tailPointer,numberOfItems
    else:
        ReturnValue = QueueArray[headPointer]
        headPointer +=1
        if headPointer >=9:
            headPointer = 0
        numberOfItems -=1
        return True,QueueArray,headPointer,tailPointer,numberOfItems,ReturnValue
    
#main
for x in range(11):
    userInput = str(input("Enter a value: "))
    result, QueueArray, headPointer, tailPointer, numberOfItems = Enqueue(QueueArray, headPointer, tailPointer, numberOfItems, userInput)
    if not result:
        print("Item not added: ")
    else:
        print("Item added")

result1,QueueArray,headPointer,tailPointer,numberOfItems,ReturnValue = Dequeue(QueueArray,headPointer,tailPointer,numberOfItems)
print(ReturnValue)
result1,QueueArray,headPointer,tailPointer,numberOfItems,ReturnValue = Dequeue(QueueArray,headPointer,tailPointer,numberOfItems)
print(ReturnValue)
