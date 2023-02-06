class Shape():
    def __init__(self):
        self.ar=0
    def area(self):
        return self.ar

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.ar=self.length*self.width

a=Rectangle(2,4)
print(a.area())