global Animals # Array 10 elements STRING
Animals = []
Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")

def SortDecending():
    Arraylength = 10
    for x in range(0,Arraylength-1):
        for y in range(0,Arraylength-x-1):
            if Animals[y][0] < Animals[y+1][0]:
                temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = temp

SortDecending()
for _ in range(0,10):
    print(Animals[_])