def fact(x,y):
    if x==0:
        return y
    else :
        return fact(x-1,y+1)

print(fact(3,0))