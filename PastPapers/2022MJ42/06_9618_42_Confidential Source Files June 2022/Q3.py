cardArray = [0 for i in range (30)]
print(cardArray)
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
def chooseCard():
    global cardArray
    flagContinue = True
    while flagContinue:
        userCard = int(input("Enter a card number: "))
        if userCard < 1 or userCard > 30:
            print("Number must be between 1 and 30")
        elif NumberChosen[userCard-1]:
            
filename = "CardValues.txt"
try:
    with open(filename,"r") as File:
        for x in range(30):
            Number = int(File.readline())
            Colour = File.readline().strip()
            cardArray[x] = card(Number, Colour)
except FileNotFoundError:
    print("file not found")
print(cardArray)
NumberChosen = [False for i in range(30)]
print(NumberChosen)