class Easy():
    '''output,input string'''
    def __init__(self):
        self.somestring=''
    def getString(self):
        self.somestring=input()
    def printString(self):
        print(self.somestring.upper(), end='')

a=Easy()
a.getString()
a.printString()



        


        


