def Unknown(x,y):
    if x<y:
        print(str(x+y))
        return Unknown(x+1,y)*2
    elif x == y:
        return 1
    else:
        print(x+y)
        return Unknown(x-1,y)//2
print("10,15")
print(str(Unknown(10,15)))
print("10,10")
print(str(Unknown(10,10)))
print("15 ,10")
print(str(Unknown(15,10)))

def UnknownIterative(x,y):
    total = 1
    while x!=y:
        print(str(x+y))
        if x < y:
            x = x+1
            total = total *2
        else:
            x = x-1
            total = int(total/2)
    return total

print("10 and 15") 
print(str(UnknownIterative(10, 15))) 
print("10 and 10") 
print(str(UnknownIterative(10, 10))) 
print("15 and 10") 
print(str(UnknownIterative(15, 10)))