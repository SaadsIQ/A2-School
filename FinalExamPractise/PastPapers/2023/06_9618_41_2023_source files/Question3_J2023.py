global Animal #ARRAY 20 ELEMENTS OF STRING
global Colour #ARAY 10 ELEMENTS OF STIRNG
Animal = [None for i in range(20)] #ARRAY 20 ELEMENTS OF STRING
Colour = [None for i in range(10)] #ARAY 10 ELEMENTS OF STIRNG
AnimalTopPointer = 0 #INTEGER
ColourTopPointer = 0 #INTEGER

def PushAnimal(DataToPush):
    global Animal, AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True

def PopAnimal():
    global AnimalTopPointer,Animal
    ReturnData = ""
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer-1]
        Animal[AnimalTopPointer-1] = None
        AnimalTopPointer -= 1
        return ReturnData
    
def readData():
    FileName = "AnimalData.txt"
    FileName2 = "ColourData.txt"
    try:
        with open(FileName,"r") as File:
            for line in File:
                DataToPush = line.strip()
                PushAnimal(DataToPush)
    except FileNotFoundError:
        print("File not found")
    try:
        with open(FileName2,"r") as File2:
            for line2 in File2:
                DataToPush2 = line2.strip()
                PushColour(DataToPush2)
    except FileNotFoundError:
        print("File not found")
def PushColour(DataToPush):
    global Colour,ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True

def PopColour():
    global Colour, ColourTopPointer
    ReturnValue = ""
    if ColourTopPointer == 0:
        return ReturnValue
    else: 
        ReturnValue = Colour[ColourTopPointer-1]
        ColourTopPointer -=1
        return ReturnValue

def OutputItem():
    global Animal, Colour, AnimalTopPointer, ColourTopPointer
    animalPopped = PopAnimal()
    colourPopped = PopColour()
    if colourPopped == "":
        PushAnimal(animalPopped)
        print("No Colour")
    elif animalPopped == "":
        PushColour(colourPopped)
        print("No animal")
    else:
        print(colourPopped, animalPopped)

print(Animal)
print(Colour)
readData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()
