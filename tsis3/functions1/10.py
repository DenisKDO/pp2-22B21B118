list1=list(map(int,input().split()))
list2=[]
def uniq(list1,list2):
    for i in list1:
        if not i in list2:
            list2.append(i)
    return list2
print(uniq(list1,list2))