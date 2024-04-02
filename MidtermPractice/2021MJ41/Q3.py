class TreasureChest:
    def __init__(self,question,answer,points):
        self.__question = question
        self.__answer = int(answer)
        self.__points = int(points)
    def getQuestion(self):
        return self.__question
    def checkAnswer(self, useranswer):
        return useranswer == self.__answer
    def getPoints(self,attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return int(self.__points/2)
        elif attempts == 3 or attempts ==4:
            return int(self.__points/4)
        else:
            return 0

def readata():
    Filename = "TreasureChestData.txt"
    arrayTreasure = []
    try:
        file = open(Filename,"r")
        dataFetched = (file.readline()).strip()
        while dataFetched != "":
            question = dataFetched
            answer = (file.readline()).strip()
            points = (file.readline()).strip()
            arrayTreasure.append(TreasureChest(question,answer,points))
            dataFetched = (file.readline()).strip()
        file.close
    except FileNotFoundError:
        print("File not found")
    return arrayTreasure

arrayTreasure = readata()
if arrayTreasure:
    qExists = False
    attempts = 1
    answerCheck = False
    while not qExists:
        qNum = int(input("Enter the question number: "))
        if 1<= qNum <=5:
            qExists = True
            while not answerCheck:
                print(arrayTreasure[qNum-1].getQuestion())
                userAnswer = int(input("Enter the answer: "))
                correct = arrayTreasure[qNum-1].checkAnswer(userAnswer)
                if correct:
                    answerCheck = True
                    point = arrayTreasure[qNum-1].getPoints(attempts)
                    print("You got this many points:", point)
                else:
                    attempts += 1