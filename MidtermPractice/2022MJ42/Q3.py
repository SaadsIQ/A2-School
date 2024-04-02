class Card:
    def __init__(self,number,colour):
        #number as INTEGER
        #Colour as STRING
        self.__number = number
        self.__colour = colour
    def GetNumber(self):
        return self.__number
    def GetColour(self):
        return self.__colour
    
CardArray = [0 for x in range(30)]
    
def ChooseCard():
    global NumberChosen
    flagContinue = True
    while flagContinue:
        usercard = int(input("Enter a card number: "))
        if usercard<1 and usercard>30:
            print("Card must be between 1 and 30")
        elif NumberChosen[usercard-1]:
            print("Card already chosen")
        else:
            print("Card chosen: ", usercard)
            flagContinue = False
            NumberChosen[usercard-1] = True
    return usercard - 1

filename = "CardValues.txt"
try:
    with open(filename,"r") as File:
        for x in range(30):
            number = int(File.readline())
            colour = File.readline().strip()
            CardArray[x] = Card(number,colour)
except FileNotFoundError:
    print("File not found")

NumberChosen = [False for i in range(30)]
player1 = []

for x in range(0,4):
    ReturnNumber = ChooseCard()
    player1.append(CardArray[ReturnNumber])
for x in range(0,4):
    print(player1[x].GetNumber())
    print(player1[x].GetColour())
