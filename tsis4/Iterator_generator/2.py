a=int(input("Enter some number: "))
b=(i for i in range(1,a+1) if i%2==0)
print(*b,sep=', ')