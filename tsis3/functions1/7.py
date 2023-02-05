a=list(map(int,input().split()))
def has_33():
    for i in range(len(a)):
        if a[i]==3 and a[i+1]==3:
            return True
    return False
print(has_33())
            