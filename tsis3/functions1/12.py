l=list(map(int,input().split()))
def histogram(l):
    for i in l:
        if i==l[len(l)-1]:
            print('*'*i,end='')
            break
        print('*'*i)
histogram(l)
