items = [54,53,62,67,86,42,7]
n = len(items)

for index in range(1,n):
    currentItem = items[index]
    index2 = index - 1
    while index2 >= 0 and currentItem < items[index2]:
        items[index2 +1] = items[index2]
        index2 -=1
        items[index2 +1] = currentItem

#print(items)