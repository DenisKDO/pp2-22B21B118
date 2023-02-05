s=input()
def ispal(s):
    count=0
    for i in range(len(s)):
        if s[i]==s[len(s)-1-i]:
            count+=1
    if count==len(s):
        return True
    return False
print(ispal(s))
