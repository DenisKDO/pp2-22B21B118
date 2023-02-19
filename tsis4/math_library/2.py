import math
def areaoftrap(h,b1,b2):
    a=(0.5*h)*(b1+b2)
    return a
a=float(input("Height: "))
b=float(input("Base, first value: "))
c=float(input("Base, second value: "))
print("Expected Output:",areaoftrap(a,b,c),sep=' ')