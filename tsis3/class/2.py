class Shape():
    def __init__(self):
        self.ar=0
    def area(self):
        return self.ar

class Square(Shape):
    def __init__(self,length):
        self.length=length
        self.ar=self.length**2

a=Shape()
print(a.area())
b=Square(2)
print(b.area())


