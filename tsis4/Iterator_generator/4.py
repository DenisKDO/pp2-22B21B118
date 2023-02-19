def squares(a,b):
    for i in range(a,b+1):
        yield i**2
a,b=input().split()
a,b=int(a),int(b)
for k,v in enumerate(squares(a,b),a):
    print(k,v,sep='-')