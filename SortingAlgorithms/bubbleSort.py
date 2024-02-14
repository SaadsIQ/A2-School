def bubbleSort():
    flag = True
    while flag:
        flag = False
        for i in range(0, n-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag = True

array = [42, 17, 89, 5, 73, 28, 64, 11, 36, 50]
n = len(array)
bubbleSort()            
print(array)
