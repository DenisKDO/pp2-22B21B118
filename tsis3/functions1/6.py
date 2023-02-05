s=input()
def rev(s): 
    s=s.split()
    s.sort(reverse=True)
    s=' '.join(s)
    return(s)
print(rev(s))