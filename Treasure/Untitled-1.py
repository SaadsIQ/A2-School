class TreasureChest:
    def __init__(self, question, answer, points):
        self.question = question  # string
        self.answer = int(answer)  # integer
        self.points = int(points)  # integer

    def getQuestion(self):
        return self.question

    def checkAnswer(self, userAnswer):
        return userAnswer == self.answer

    def getPoints(self, attempts):
        if attempts == 1:
            return self.points
        elif attempts == 2:
            return int(self.points / 2)
        elif attempts == 3 or attempts == 4:
            return int(self.points / 4)
        else:
            return 0

def readData():
    FileName = "TreasureChestData.txt"
    arrayTreasure = []
    try:
        with open(FileName, "r") as File:
            for line in File:
                question = line.strip()
                answer = File.readline().strip()
                points = File.readline().strip()
                arrayTreasure.append(TreasureChest(question, answer, points))
    except FileNotFoundError:
        print("File Not Found")
    return arrayTreasure

def main():
    arrayTreasure = readData()
    if arrayTreasure:
        qExists = False
        Attempts = 1
        AnswerCheck = False
        while not qExists:
            qNum = int(input("Enter the question number: "))
            if 1 <= qNum <= 5:
                qExists = True
                while not AnswerCheck:
                    print(arrayTreasure[qNum - 1].getQuestion())
                    userAnswer = int(input("Enter your answer: "))
                    Correct = arrayTreasure[qNum - 1].checkAnswer(userAnswer)
                    if Correct:
                        AnswerCheck = True
                        Point = arrayTreasure[qNum - 1].getPoints(Attempts)
                        print("You got this many points:", Point)
                    else:
                        Attempts += 1


if __name__ == "__main__":
    main()
