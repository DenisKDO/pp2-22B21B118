def ex(heads,legs):
    a=heads*2
    b=legs-a
    rabbits=b/2
    chickens=heads-rabbits
    print(f"Chickens: {int(chickens)}, rabbits: {int(rabbits)}")
while True:
    a=int(input("Heads: "))
    b=int(input("Legs: "))
    ex(a,b)