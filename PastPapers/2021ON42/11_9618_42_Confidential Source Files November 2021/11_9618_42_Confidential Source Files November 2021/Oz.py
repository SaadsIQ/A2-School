'''
def Unknown(X, Y): 
 if X < Y: 
    print(str(X + Y)) 
    return Unknown(X + 1, Y) * 2 
 elif X == Y: 
    return 1 
 else: 
    print(str(X + Y)) 
    return int(Unknown(X - 1, Y) / 2) 
print("10 and 15") 
print(str(Unknown(10, 15))) 
print("10 and 10") 
print(str(Unknown(10, 10))) 
print("15 and 10") 
print(str(Unknown(15, 10))) 

def IterativeUnknown(X,Y): 
 Total = 1 
 while X != Y: 
    print(str(X + Y)) 
    if X < Y: 
         X = X + 1 
         Total = Total * 2 
    else: 
         X = X - 1 
         Total = int(Total / 2) 
 return Total 
print("10 and 15") 
print(str(IterativeUnknown(10, 15))) 
print("10 and 10") 
print(str(IterativeUnknown(10, 10))) 
print("15 and 10") 
print(str(IterativeUnknown(15, 10))) 

class Picture:
    def __init__(self, description, width, height, frame_color):
        self.__Description = description  # string
        self.__Width = int(width)  # integer
        self.__Height = int(height)  # integer
        self.__FrameColour = frame_color  # string

    def GetDescription(self):
        return self.__Description

    def GetWidth(self):
        return self.__Width

    def GetHeight(self):
        return self.__Height

    def GetColour(self):
        return self.__FrameColour

PictureArray = [Picture("", 0, 0, "") for _ in range(100)]

def ReadData(PictureArray):
    Filename = "Pictures.txt"
    Counter = 0
    try:
        with open(Filename, "r") as File:
            for line in File:
                description = line.strip().lower()
                width = int(File.readline().strip())
                height = int(File.readline().strip())
                frame = File.readline().strip().lower()
                PictureArray[Counter] = Picture(description, width, height, frame)
                Counter += 1
    except IOError:
        print("Could not find File")
    return Counter, PictureArray

NumberPicturesInArray, PictureArray = ReadData(PictureArray)

FrameColour = input("Input the Frame colour ").lower()
MaxWidth = int(input("Input the Maximum Width "))
MaxHeight = int(input("Input the Maximum Height "))

print("Matches Frames shown")
for Z in range(NumberPicturesInArray):
    if PictureArray[Z].GetColour() == FrameColour:
        if PictureArray[Z].GetWidth() <= MaxWidth:
            if PictureArray[Z].GetHeight() <= MaxHeight:
                print(PictureArray[Z].GetDescription(), str(PictureArray[Z].GetWidth()), str(PictureArray[Z].GetHeight()))
'''
ArrayNodes = [[0 for X in range(3)] for Y in range(20)]
RootPointer = -1
FreeNode = 0

def AddNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Enter the Data: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1

        if RootPointer == -1:  # Add to start
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while not Placed:
                if NodeData < ArrayNodes[CurrentNode][1]:
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
        FreeNode += 1  # Increment FreeNode outside the else block
    else:
        print("Tree is full")
    return ArrayNodes, RootPointer, FreeNode

def PrintAll(ArrayNodes):
    for X in range(20):
        print("{:<5} {:<5} {:<5}".format(ArrayNodes[X][0], ArrayNodes[X][1], ArrayNodes[X][2]))

for X in range(10):
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)

PrintAll(ArrayNodes)

def InOrder(ArrayNodes, RootNode):
    if ArrayNodes[RootNode][0] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][0])
    print(str(ArrayNodes[RootNode][1]))  # Print the node data
    if ArrayNodes[RootNode][2] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][2])

InOrder(ArrayNodes, RootPointer)
 