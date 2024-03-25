import random
arrayLength = 10
arrayData = [[random.randint(0,100)for i in range(arrayLength)]for j in range(arrayLength)]
def printMethod():
    for x in range(0, 10):
        for y in range(0, 10):
            print(arrayData[x][y], " ", end='')
        print("") 
printMethod()
for x in range(0,arrayLength):
    for y in range(0,arrayLength):
        for z in range(0, arrayLength -y- 1):
            if arrayData[x][z]>arrayData[x][z+1]:
                arrayData[x][z], arrayData[x][z+1] = arrayData[x][z+1], arrayData[x][z]
print("///")                
printMethod()

def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower+(Upper+1))//2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
    return -1
SearchValue = int(input("Enter a value:"))
print(BinarySearch(arrayData,0,arrayLength-1,SearchValue))