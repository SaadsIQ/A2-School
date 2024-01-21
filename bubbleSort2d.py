name = [["Smithfield","Tom"],["John","Smith"],["David","Johnson"],["Emma","Jones"],["Christopher","Miller"]]
score = [24,55,68,84,100]
student = len(name)
flag = True

while flag:
    flag = False
    for x in range(0, student-1):
        if score[x] < score [x+1]:
            score[x],score[x+1] = score[x+1], score[x]
            name[x],name[x+1] = name[x+1],name[x]
            flag = True
print(name)
print(score)
