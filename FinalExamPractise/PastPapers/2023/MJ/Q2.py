class SaleData:
    def __init__(self,SaleID,quantity):
        self.saleID = SaleID #STRING
        self.saleQuantity = quantity #INTEGER

circularQueue = [] # Array saledata 5 items
Head = 0
Tail = 0
NumberOfItems = 0
for x in range (0,5):
    circularQueue.append(SaleData("",-1))

def Enqueue(value):
    global circularQueue,Head,Tail,NumberOfItems
    if NumberOfItems == 5:
        return -1
    else:
        circularQueue[Tail] = value
        if Tail == 4:
            Tail = 0
        else:
            Tail +=1
        NumberOfItems +=1
        return 1
        
def Dequeue():
    global circularQueue,Head,Tail,NumberOfItems
    recordRemoved = SaleData("",-1)
    if NumberOfItems == 0:
        return recordRemoved
    else:
        recordRemoved = circularQueue[Head]
        NumberOfItems -= 1
        if Head == 4:
            Head = 0
        else:
            Head += 1
        return recordRemoved
    
def EnterRecord():
    ID = input("Enter ID: ")
    Quantity = int(input("Enter quantity: "))
    item = SaleData(ID,Quantity)
    if Enqueue(item) == -1:
        print("Full")
    else:
        print("Stored")

EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
returnValue = Dequeue()
if returnValue.saleID == "":
    print("No items")
else:
    print("Removed record: ",returnValue.saleID,returnValue.saleQuantity)
EnterRecord()
for x in range(0,5):
    print("ID: ",circularQueue[x].saleID,"Quantity",circularQueue[x].saleQuantity)