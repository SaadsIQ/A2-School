class Picture:
    def __init__(self, Description, Width, Height, FrameColour):
        self.__Description = Description #STRING
        self.__Width = Width #INTEGER
        self.__Height = Height #INTEGER
        self.__FrameColour = FrameColour #STRING
    
    def GetDescription(self):
        return self.__Description
    def GetWidth(self):
        return self.__Width
    def GetHeight(self):
        return self.__Height
    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, Description):
        self.__Description = Description

def readData(PictureArray):
    fileName = "Pictures.txt"
    counter = 0
    try:
        with open(fileName,"r") as File:
            for line in File:
                Description = line.strip().lower()
                Width = int(File.readline().strip())
                Height = int(File.readline().strip())
                FrameColour = File.readline().strip().lower()
                PictureArray[counter] = Picture(Description,Width,Height,FrameColour)
                counter = counter+1
    except FileNotFoundError:
            print("File not found")
    return counter, PictureArray

def printArray():
    index1 = 0
    for _ in range(NumberPicturesInArray):
        print(PictureArray[index1].GetColour(),PictureArray[index1].GetWidth(),PictureArray[index1].GetHeight(),PictureArray[index1].GetDescription())
        index1 += 1

PictureArray = [Picture("",0,0,"") for x in range(0,100)]

NumberPicturesInArray, PictureArray = readData(PictureArray)

print(NumberPicturesInArray)
printArray()

usercolour = str(input("Enter a color to search for: ")).lower()
userWidth = int(input("Enter the maximum width: "))
userHeight = int(input("Enter the maximum height: "))

for x in range(NumberPicturesInArray):
    if PictureArray[x].GetColour() == usercolour:
        if PictureArray[x].GetWidth() <= userWidth:
            if PictureArray[x].GetHeight() <= userHeight:
                print(PictureArray[x].GetDescription(), PictureArray[x].GetWidth(), PictureArray[x].GetHeight(), PictureArray[x].GetColour())