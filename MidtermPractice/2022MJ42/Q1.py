def PrintValues():
    global StackData, StackPointer
    print(StackPointer)
    for x in range(10):
        print(StackData[x])
def Push(Value):
    global StackData, StackPointer
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = Value
        StackPointer += 1
        return True
def Pop():
    global StackData,StackPointer
    if StackPointer == 0:
        return -1
    else:
        valueReturned = StackData[StackPointer-1]
        StackPointer -=1
        StackData[StackPointer] = 0
        return valueReturned

global StackData
global StackPointer
StackData  =[0 for x in range(10)]
StackPointer = 0
print(StackData)
for x in range(0,11):
    Value = int(input("Enter a number to Push: "))
    if Push(Value) == True:
        print(Value, "Added to stack")
    else: 
        print("Stack full")
print(StackData)
Pop()
Pop()
print(StackData)
