def gen(n):
    for i in range(n,-1,-1):
        yield i
a=int(input("Enter some number: "))
for i in gen(a):
    print(i)