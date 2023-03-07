import os
a=input('Enter path: ')
if os.path.exists(a):
    print(os.path.basename(a),os.path.dirname(a),sep='\n')
else:
    print(r"File doesn't exist")