class Easy():
    '''output,input string'''
    def __init__(self):
        self.somestring=''
    def getstring(self):
        self.somestring=input()
    def printstring(self):
        print(self.somestring,end=' ')

string=Easy()
string.getstring()
string.printstring()


        


