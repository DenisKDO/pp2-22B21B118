import math
def areaofregularpol(n,l):
    return (n*(l**2))/(4*(math.tan(math.pi/n)))
n=int(input("Input number of sides: "))
l=int(input("Input the length of a side: "))
print("The area of the polygon is:", round(areaofregularpol(n,l)),sep=' ')