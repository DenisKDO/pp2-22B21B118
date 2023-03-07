with open('text.txt','r') as file:
    count=0
    for i in file:
        count+=1
print('Lines in file:',count)