class Balloon:
    def __init__(self, DefenceItem, Colour):
        self.__DefenceItem = DefenceItem #STRING
        self.__Colour = Colour #STRING
        self.__Health = 100 #INTEGER
    def GetDefenceItem(self):
        return self.__DefenceItem
    def ChangeHealth(self, change):
        self.__Health = self.__Health + change
    def CheckHealth(self):
        if self.__Health <=0:
            return True
        else:
            return False
        
#main
userDefenceItem = input("Enter a defence item: ")
userBalloonColour = input("Enter a balloon colour: ")
Balloon1 = Balloon(userDefenceItem,userBalloonColour)

def Defend(myBalloon):
    opponentStrength = int(input("Enter opponenet stength: "))
    myBalloon.ChangeHealth(-opponentStrength)
    print("You defended with",str(myBalloon.GetDefenceItem()))
    if myBalloon.CheckHealth():
        print("No health remaining")
    else:
        print("Defence succeeded")
    return myBalloon


Defend(Balloon1)