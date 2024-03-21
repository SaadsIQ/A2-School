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
