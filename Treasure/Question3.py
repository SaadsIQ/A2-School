class TreasureChest:
    #Private question: String
    #Private answer: Integer
    #Private points: Integer
    def __init__(self, question, answer, points):
        self.question = question
        self.answer = answer
        self.points = points
    #arrayTreasure(5) as treasureChest
def readData():
    FileName = "TreasureChestData.txt"
    arrayTreasure = []
    try: 
        file = open(FileName, "r")
        dataFetched  = (file.readline()).strip()
        while dataFetched!= "":
            question = dataFetched
            answer = (file.readline()).strip()
            points = (file.readline()).strip()
            arrayTreasure.append(TreasureChest(question, answer, points))
            dataFetched = (file.readline()).strip()
        file.close()
    except IOError:
        print("file not found")
def main():
    def getQuestion():
        return Question


#readdata = readData()
"""
for treasure in readdata:
    print("Question:", treasure.question)
    print("Answer:", treasure.answer)
    print("Points:", treasure.points)
    print()
"""