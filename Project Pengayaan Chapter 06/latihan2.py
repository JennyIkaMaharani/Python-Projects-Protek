import math
def pangkat(a,b):
    x = a
    while (x < b):
        y = x**2
        print(y, end=" ")
        x += 1
def sqNumber(a,b):
        j= round(a**(1/2))+1
        k= round(b**(1/2)) +1
        pangkat(j,k)
        print("")

