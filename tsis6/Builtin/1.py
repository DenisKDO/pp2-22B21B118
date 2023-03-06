list=list(map(int,input().split()))
def mult(l):
    pr=1
    for i in l:
        pr=pr*i
    return pr
print(mult(list))