class Picture:
    def __init__(self, Description, Width, Height, FrameColour):
        self.__Description = Description #STRING
        self.__Width = Width #INTEGER
        self.__Height = Height #INTEGER
        self.__FrameColour = FrameColour #STRING
    
    def GetDescription(self):
        return self.__Description
    def GetHeight(self):
        return self.__Height
    def GetWidth(self):
        return self.__Width
    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, Description):
        self.__Description = Description

def readData(PictureArray):
    fileName = "Pictures.txt"
    counter = 0
    try:
        with open(fileName,"r") as File:
            Description = File.readline().strip().lower()
            Width = int(File.readline()).strip()
            Height = int(File.readline()).strip()
            FrameColour = File.readline().strip().lower()
            PictureArray[counter] = picture(Description,Width,Height,FrameColour)
            counter += 1
    except FileNotFoundError:
            print("File not found")
    return counter, PictureArray

PictureArray = [Picture("",0,0,"") for x in range(0,100)]
print(PictureArray)
readData()