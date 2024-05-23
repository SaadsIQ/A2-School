
FileData = [[""]*2 for i in range(11)]
"""
def ReadHighScores():
    global FileData
    FileName = "HighScore.txt"
    try:
        with open(FileName,"r") as File:
            for x in range(11):
                FileData[x][0] = File.readline().strip()
                FileData[x][1] = File.readline().strip()
    except FileNotFoundError:
        print("File not found")

def OutputHighScores():
    global FileData
    for  i in range(0,len(FileData)):
        print(FileData[i][0], FileData[i][1])

ReadHighScores()
OutputHighScores()

userName = input("Enter a user name: ")
while len(userName) != 3:
    userName = input("Enter a user name: ")
userScore = int(input("Enter your score: "))
while int(userScore) <1 or int(userScore) >100000:
    userScore = int(input("Enter your score: "))

def Arrange(Username, Score):
    for x in range(0, 10):
        if Score > int(FileData[x][1]):
            Temp1 = FileData[x][0]
            Temp2 = FileData[x][1]
            FileData[x][0] = Username
            FileData[x][1] = Score
            Count = x+1
            while(Count < 10):
                Second1 = FileData[Count][0]
                Second2 = FileData[Count][1]
                FileData[Count][0] = Temp1
                FileData[Count][1] = Temp2
                Temp1 = Second1
                Temp2 = Second2
                Count = Count + 1
                break;
Arrange(userName,userScore)
print(FileData)
"""
def read_high_scores(filename="HighScore.txt"):
    data = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                name = lines[i].strip()
                score = lines[i + 1].strip()
                data.append([name, int(score)])
    except FileNotFoundError:
        print("File not found")
    return data

def output_high_scores(data):
    for name, score in data:
        print(name, score)

def arrange_high_scores(data, username, score):
    data.append([username, score])
    data.sort(key=lambda x: x[1], reverse=True)  # Sort descending by score
    if len(data) > 10:
        data.pop()  # Keep only the top 10
    return data


file_data = read_high_scores()
output_high_scores(file_data)

username = input("Enter a user name: ")
while len(username) != 3:
    username = input("Please enter a 3-letter user name: ")
    
user_score = int(input("Enter your score: "))
while not (1 <= user_score <= 100000):
    user_score = int(input("Enter a valid score (1-100000): "))

file_data = arrange_high_scores(file_data, username, user_score)
output_high_scores(file_data)

def writeTopten():
    filename = open("NewHighScore.txt","w")
    for x in range(10):
        filename.write(str(FileData[x][0])+"\n")
        filename.write(str(FileData[x][1])+"\n")
        filename.close()