Card = [0 for i in range (30)]
print(Card)
class card:
    #Number as Integer
    #Colour as String
    def __init__(self, Number, Colour):
        self.__Number = Number
        self.__Colour = Colour
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
def addData():
    global Card
    filename = "CardValues.txt"
    try:
        with open(filename,"r") as File:
            for line in File:
                Number = line.strip()
                Colour = File.readline().strip()
                Card.append(card(Number, Colour))
    except FileNotFoundError:
        print("file not found")
    return Card
addData()
print(Card)