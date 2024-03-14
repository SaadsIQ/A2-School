arrayData = [10,5,6,7,1,12,13,15,21,8]
data = int(input("Enter a number: "))
def linearSearch(data):
    for index in range(len(arrayData)):
        if arrayData[index] == data:
            return True
    return False

printSearchResults = linearSearch(data)
if printSearchResults:
    print("Found")
else: 
    print("Not found")