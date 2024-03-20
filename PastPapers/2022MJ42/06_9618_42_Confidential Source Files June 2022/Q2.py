import random
arrayLength = 10
arrayData = [[random.randint(0,100)for i in range(arrayLength)]for j in range(arrayLength)]
def printMethod():
    global arrayData
    for i in arrayData:
        print(i)
printMethod()
for x in range(0,arrayLength):
    for y in range(0,arrayLength):
        for z in range(0, arrayLength -y- 1):
            if arrayData[x][z]>arrayData[x][z+1]:
                arrayData[x][z], arrayData[x][z+1] = arrayData[x][z+1], arrayData[x][z]
print("///")                
printMethod()

def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper>= Lower:
        Mid = (lower+(upper-1))/2
        if SearchArray[0,Mid] == SearchValue:
            return middle
        else:
            if SearchArray[0,Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower)