intArray = [1,2,3,4,5,6,7,8,9,10]
toFind = int(input("Enter the item to find: "))
found = False
start = 0 
end = len(intArray) - 1

while start <= end and found == False:
    mid = (start+end)//2
    if intArray[mid] == toFind:
        found = True
    else:
        if intArray[mid] < toFind:
            start = mid + 1
        else:
            end = mid -1
if found == True:
    print("Item found at index:", mid)
else:
    print("Item not in list")