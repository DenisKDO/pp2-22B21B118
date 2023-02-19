def func(n):
    for i in range(1,n+1):
        if i%3==0 and i%4==0:
            yield i
a=int(input("Enter some number: "))
for i in func(a):
    print(i)
    