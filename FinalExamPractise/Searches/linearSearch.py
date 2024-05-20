intArray = [1,2,5,7,4,8,3]

def linearSearch(intArray):
    searchItem = int(input("Enter the item to search for: "))
    arrLength = len(intArray)
    counter = 0
    while counter != arrLength:
        if intArray[counter] == searchItem:
            print("Found",counter)
            break
        else:
            counter += 1
        if counter == arrLength:
            print("Not in list")
linearSearch(intArray)