DataArray = [] # ARRAY 25 ELEMENTS INTEGER

fileName = "Data.txt"
try:
    with open(fileName,"r") as File:
        for line in File:
            DataArray.append(int(line))
except FileNotFoundError:
    print("File not found")

def PrintArray(dataArray):
    output = ""
    for x in range(0,len(dataArray)):
        output = output + str(dataArray[x])+" "
    print(output)
PrintArray(DataArray)

def LinearSearch(dataArray, searchValue):
    count = 0
    index = 0
    maxSize = len(dataArray)
    while index != maxSize:
        if dataArray[index] == searchValue:
            count += 1
        index += 1
    if count == 0:
        return count
    return count
    
userInput = int(input("Enter a value between 0 and 100 inclusive: "))
while userInput<0 or userInput>100:
    userInput = int(input("Enter a value between 0 and 100 inclusive: "))
numberOfTimes = LinearSearch(DataArray,userInput)
print("The number", userInput, "is found", numberOfTimes, "times")