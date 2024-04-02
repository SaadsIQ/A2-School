arrayData = [10,5,6,7,1,12,13,15,21,8]

def linearsearch(userValue):
    global arrayData
    for index in range(len(arrayData)):
        if arrayData[index] == userValue:
            return True
    return False
userValue = int(input("Enter a Number: "))
searchResult = linearsearch(userValue)
if searchResult:
    print("Found")
else:
    print("Not found")


def bubbleSort():
    temp = None
    for x in range(0,len(arrayData)):
        for y in range(0,len(arrayData)-1):
            if arrayData[y] > arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp
                
print(arrayData)
bubbleSort()
print(arrayData)