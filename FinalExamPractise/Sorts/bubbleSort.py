intArray = [5,24,12,64,78,99,10,53]

def bubbleSort(intArray):
    arrayLength = len(intArray)
    for i in range(arrayLength-1):
        for j in range(arrayLength-i-1):
            if intArray[j]> intArray[j+1]:
                intArray[j],intArray[j+1] = intArray[j+1], intArray[j]
    print(intArray)
bubbleSort(intArray)