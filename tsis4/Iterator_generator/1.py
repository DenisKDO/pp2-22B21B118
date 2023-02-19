a=int(input("Enter some number: "))
b=(i**2 for i in range(1,a+1))
for k,v in enumerate(b):
    print(k+1,v,sep='-')
