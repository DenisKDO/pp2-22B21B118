import math
r=int(input("Enter r of sphere: "))
def s(r):
    return 4/3*math.pi*r**3
print(round(s(r),3))