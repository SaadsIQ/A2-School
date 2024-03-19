def OutputValues():
    print("StackPointer: ", StackPointer)
    for x in range(0,10):
        print(StackData[x])
def Push(userInput):
    global StackData, StackPointer
    if StackPointer == maxStack:
        return False
    else:
        StackData[StackPointer] = userInput
        StackPointer += 1
        return True
def Pop():
    global StackData, StackPointer
    if StackPointer == 0:
        Return -1
    elif StackPointer <= maxStack:
        StackPointer -=1
        valueTop = StackData[StackPointer]
        StackData[StackPointer] = 0
        return valueTop
global StackData #integer
global StackPointer
StackData = [0,0,0,0,0,0,0,0,0,0] #integer
StackPointer = 0
maxStack = 10
for x in range(0,11):
    userInput = int(input("Enter a number to push: "))
    if Push(userInput) == True:
        print("Added")
    else:
        print("Stack full")
OutputValues()
print(StackData)
Pop()
Pop()
Pop()
Pop()
print(StackData)
print(Pop)