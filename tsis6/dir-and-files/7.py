import os
with open('text.txt','r') as file:
    f=file.read()
with open('test.txt','w') as newfile:
    newfile.write(f)