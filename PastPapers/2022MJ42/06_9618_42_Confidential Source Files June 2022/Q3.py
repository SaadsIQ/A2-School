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

cardArray = [0 for i in range (30)]

def chooseCard():
    global NumberChosen
    flagContinue = True
    while flagContinue:
        userCard = int(input("Enter a card number: "))
        if userCard < 1 or userCard > 30:
            print("Number must be between 1 and 30")
        elif NumberChosen[userCard-1]:
            print("Card already chosen")
        else:
            print("Card chosen: ", userCard)
            flagContinue = False
            NumberChosen[userCard-1] = True
    return userCard - 1

filename = "CardValues.txt"
try:
    with open(filename,"r") as File:
        for x in range(30):
            Number = int(File.readline())
            Colour = File.readline().strip()
            cardArray[x] = card(Number, Colour)
except FileNotFoundError:
    print("file not found")

NumberChosen = [False for i in range(30)]
Player1 = []

for x in range(0,4):
    player1num = chooseCard()
    Player1.append(cardArray[player1num])

for x in range(0,4):
    print(Player1[x].GetNumber())
    print(Player1[x].GetColour())