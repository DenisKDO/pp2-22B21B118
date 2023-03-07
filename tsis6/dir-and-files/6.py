import os, string
os.mkdir('7task')
os.chdir('7task')
for i in string.ascii_uppercase:
    with open(i+'.txt','w') as file:
        pass
