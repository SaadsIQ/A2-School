arrayData = [10,5,6,7,1,12,13,15,21,8]
def bubblesort():
    temp = None
    for x in range(0,len(arrayData)):
        for y in range(0,len(arrayData)-1):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp
print(arrayData)
bubblesort()
print(arrayData)
