intArray = [100,1,20,5,7]
def insertionSort(intArray):
    arrayLength = len(intArray)
    # Iterate through the array starting from the second element
    for i in range(1,arrayLength):
        temp = intArray[i] # Store the current element in temp
        j = i -1 # Initialize j to the index of the last element in the sorted subarray
        while j>=0 and intArray[j]>temp:  # Move elements of the sorted subarray that are greater than temp to one position ahead
            intArray[j+1] = intArray[j] # Shift element to the right
            j -=1 # Move to the previous element
        intArray[j+1] = temp  # Insert the temp element into its correct position
    print(intArray)
insertionSort(intArray)