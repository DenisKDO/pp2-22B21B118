import os
a=input('Enter path: ')
if os.path.exists(a):
    os.remove(a)
