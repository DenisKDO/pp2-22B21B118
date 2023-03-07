import os
a=input('Input directory path: ')
print('Only directories:')
for i in os.listdir(a):
    if os.path.isdir(os.path.join(a,i)):
        print(i)
print('Only files:')
print([i for i in os.listdir(a) if os.path.isfile(os.path.join(a,i))])
print('All dirs and files: ', [i for i in os.listdir(a)],sep='\n')