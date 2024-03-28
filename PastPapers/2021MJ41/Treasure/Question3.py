class TreasureChest:
    #Private question: String
    #Private answer: Integer
    #Private points: Integer
    def __init__(self, question, answer, points):
        self.question = question
        self.answer = int(answer)
        self.points = int(points)
    #arrayTreasure(5) as treasureChest
    def getQuestion(self):
        return self.question
    def checkAnswer(self, useranswer):
        return useranswer == self.answer
    def getPoints(self, attempts):
        if attempts == 1:
            return self.points
        if attempts == 2:
            return int(self.points/2)
        if attempts == 3 or attempts == 4:
            return int(self.points/4)
        else:
            return 0
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
    return arrayTreasure
def main():
    arrayTreasure = readData()
    if arrayTreasure:
        qExits = False
        attempts = 1
        answerCheck = False
        while not qExits:
            qNum = int(input("Enter the question number: "))
            if 1<= qNum <= 5:
                qExits = True
                while not answerCheck:
                    print(arrayTreasure[qNum-1].getQuestion())
                    useranswer = int(input("enter the answer: "))
                    correct = arrayTreasure[qNum-1].checkAnswer(useranswer)
                    if correct:
                        answerCheck = True
                        point = arrayTreasure[qNum-1].getPoints(attempts)
                        print("You got this many points: ", point)
                    else:
                        attempts +=1
if __name__ == "__main__":   
    main()