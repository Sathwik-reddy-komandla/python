num=[14,23,8,12,2,5,90]

def square (num):
    return num*num

newlist=map(square,num)

print(list(newlist))