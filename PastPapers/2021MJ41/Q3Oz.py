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
        with open(FileName, "r") as file:
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
'''
class TreasureChest:: Defines a class named TreasureChest.

def __init__(self, question, answer, points):: Initializes the TreasureChest class with three attributes: question, answer, and points. These are set when a new instance of the class is created.

self.question = question # string: Sets the question attribute of the instance to the provided question.

self.answer = int(answer) # integer: Sets the answer attribute of the instance to the provided answer, converted to an integer.

self.points = int(points) # integer: Sets the points attribute of the instance to the provided points, converted to an integer.

def getQuestion(self):: Defines a method named getQuestion that returns the value of the question attribute.

return self.question: Returns the value of the question attribute.

def checkAnswer(self, userAnswer):: Defines a method named checkAnswer that takes a userAnswer as input and checks if it matches the instance's answer.

return userAnswer == self.answer: Returns True if the userAnswer matches the instance's answer, otherwise returns False.

def getPoints(self, attempts):: Defines a method named getPoints that calculates the points earned based on the number of attempts made.

if attempts == 1:: Checks if the number of attempts is equal to 1.

return self.points: If the number of attempts is 1, returns the full points of the question.

elif attempts == 2:: Checks if the number of attempts is equal to 2.

return int(self.points / 2): If the number of attempts is 2, returns half of the points of the question.

elif attempts == 3 or attempts == 4:: Checks if the number of attempts is equal to 3 or 4.

return int(self.points / 4): If the number of attempts is 3 or 4, returns one-fourth of the points of the question.

else:: If the number of attempts is not 1, 2, 3, or 4.

return 0: Returns 0 points.

def readData():: Defines a function named readData to read data from a file and create TreasureChest objects.

FileName = "TreasureChestData.txt": Assigns the filename to a variable.

arrayTreasure = []: Initializes an empty list to store TreasureChest objects.

with open(FileName, "r") as File:: Opens the file in read mode.

for line in File:: Iterates through each line in the file.

question = line.strip(): Reads the question from the file and removes any leading/trailing whitespace.

answer = File.readline().strip(): Reads the answer from the file and removes any leading/trailing whitespace.

points = File.readline().strip(): Reads the points from the file and removes any leading/trailing whitespace.

arrayTreasure.append(TreasureChest(question, answer, points)): Creates a new TreasureChest object with the read question, answer, and points, and appends it to the arrayTreasure list.

except FileNotFoundError:: Catches the exception if the file is not found.

return arrayTreasure: Returns the list of TreasureChest objects.

def main():: Defines the main function.

arrayTreasure = readData(): Calls the readData function to read the data from the file and store it in arrayTreasure.

if arrayTreasure:: Checks if arrayTreasure is not empty.

qExists = False: Initializes a variable qExists to track if the question number entered by the user exists.

Attempts = 1: Initializes a variable Attempts to track the number of attempts made by the user.

AnswerCheck = False: Initializes a variable AnswerCheck to track if the user's answer is correct.

while not qExists:: Loops until a valid question number is entered by the user.

qNum = int(input("Enter the question number: ")): Prompts the user to enter a question number and converts the input to an integer.

if 1 <= qNum <= 5:: Checks if the entered question number is between 1 and 5.

qExists = True: Sets qExists to True if the entered question number is valid.

while not AnswerCheck:: Loops until the user's answer is correct.

print(arrayTreasure[qNum - 1].getQuestion()): Prints the question corresponding to the entered question number.

userAnswer = int(input("Enter your answer: ")): Prompts the user to enter their answer and converts the input to an integer.

Correct = arrayTreasure[qNum - 1].checkAnswer(userAnswer): Checks if the user's answer is correct.

if Correct:: If the user's answer is correct.

AnswerCheck = True: Sets AnswerCheck to True.

Point = arrayTreasure[qNum - 1].getPoints(Attempts): Calculates the points earned based on the number of attempts.

print("You got this many points:", Point): Prints the points earned by the user.

else:: If the user's answer is incorrect.

Attempts += 1: Increments the number of attempts.

if __name__ == "__main__":: Checks if the script is run directly.

main(): Calls the main function.






'''