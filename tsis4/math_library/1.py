import math
def converter(d):
    return math.radians(d)
a=int(input("Input degree: "))
print("Output radian: ",round(converter(a),7))