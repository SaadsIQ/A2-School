import random

def printMethod():
    for x in range(0, 10):
        for y in range(0, 10):
            print(arrayData[x][y], " ", end='')
        print("") 
def BinarySearch(SearchArray,Lower,Upper,SearchValue):
    if Upper>=Lower:
        mid = (Lower+(Upper-1))//2
        if SearchArray[0][mid] == SearchValue:
            return mid
        else:
            if SearchArray[0][mid] > SearchValue:
                return BinarySearch(SearchArray,Lower,mid-1,SearchValue)
            else:
                return BinarySearch(SearchArray,mid+1,Upper,SearchValue)
    return -1

ArrayLength = 10
ArrayData = [[random.randint(0,100) for i in range(ArrayLength)] for j in range(ArrayLength)]
printMethod(ArrayData)
for x in range(0,ArrayLength):
    for y in range(0,ArrayLength-1):
        for z in range(0,ArrayLength-y-1):
            if ArrayData[x][z] > ArrayData[x][z+1]:
                tempValue = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z+1]
                ArrayData[x][z+1] = tempValue
print("")
printMethod(ArrayData)
SearchValue = int(input("Enter a number to search"))
print(BinarySearch(ArrayData,0,ArrayLength-1,SearchValue))
