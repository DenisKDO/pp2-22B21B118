a = list(map(int, input("Enter numbers: ").split()))
def isprime(a):
    for i in range(2,a//2+1):
        if a%i==0:
            return False
    return True
def filter_prime(a):
    for i in a:
        if isprime(i):
            print(i,end=' ')
print("Prime numbers from list: ",end='')
filter_prime(a)



                
