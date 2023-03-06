s=input()
def checker(s):
    low=0
    up=0
    for i in s:
        if i.islower():
            low+=1
        elif i.isupper():
            up+=1
        else:
            continue
    return low, up
for key,value in enumerate(checker(s)):
    if key==0:
        print(f'lower case: {value}')
    else:
        print(f'upper case: {value}')
