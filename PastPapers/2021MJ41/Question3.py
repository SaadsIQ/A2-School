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
    f = open(FileName,"r")
    arrayTreasure = []
    try: 
        File = f.readline().strip()
        while question != "":
            answer = file.readline().strip()
            points = file.readline().strip()
            arrayTreasure.append(TreasureChest(question, answer, points))
            return arrayTreasure
    except:
        return False

readdata = readData()