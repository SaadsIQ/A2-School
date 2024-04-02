class Picture:
    def __init__(self, description, width, height, frameColour):
        self.__description = description
        self.__width = int(width)
        self.__height = int(height)
        self.__frameColour = frameColour
    def GetDescription(self):
        return self.__description
    def GetWidth(self):
        return self.__width
    def GetHeight(self):
        return self.__height
    def GetColour(self):
        return self.__frameColour
    
    def SetDescription(self, description):
        self.__description = description


def ReadData():
    filename = "Pictures.txt"
    counter = 0
    try:
        with open(filename,"r") as File:
            for line in File:
                description = line.strip().lower()
                width = int(File.readline().strip())
                height = int(File.readline().strip())
                frameColour = File.readline().strip().lower()
                PictureArray[counter] = Picture(description,width,height,frameColour)
                counter += 1
    except FileNotFoundError:
        print("file not found")
    return counter, PictureArray
def printArray():
    global counter
    index1 = 0
    for _ in range(NumberPicturesInArray):
        print(PictureArray[index1].GetColour(),PictureArray[index1].GetWidth(),PictureArray[index1].GetHeight(),PictureArray[index1].GetDescription())
        index1 += 1

PictureArray = [Picture("",0,0,"") for x in range(0,100)]
NumberPicturesInArray, PictureArray = ReadData()
printArray()

usercolor, userWidth , userHeight = str(input("Enter color: ").lower()),int(input("Enter width: ")), int(input("Enter height: "))
print(usercolor,userWidth,userHeight)
for x in range(NumberPicturesInArray):
    if PictureArray[x].GetColour() == usercolor:
        if PictureArray[x].GetWidth() <= userWidth:
            if PictureArray[x].GetHeight() <= userHeight:
                print(PictureArray[x].GetDescription(),PictureArray[x].GetWidth(),PictureArray[x].GetHeight(),PictureArray[x].GetColour())


for x in range(NumberPicturesInArray):
    if PictureArray[x].GetColour() == usercolor:
        if PictureArray[x].GetWidth() <= userWidth:
            if PictureArray[x].GetHeight() <= userHeight:
                print(PictureArray[x].GetDescription(), PictureArray[x].GetWidth(), PictureArray[x].GetHeight())

