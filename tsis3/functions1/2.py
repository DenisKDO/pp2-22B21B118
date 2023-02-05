def ftoc(F):
    return 5/9*(F-32)
while True:
    F=int(input("Enter temperature in F: "))
    print("Yout temperature in C: ",round(ftoc(F),2))


