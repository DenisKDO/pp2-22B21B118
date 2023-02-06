class Point:
    def __init__(self,xcoord,yccord):
        self.xcoord=xcoord
        self.ycoord=yccord
    def show(self):
        print(f"Coordinates of point ({self.xcoord};{self.ycoord})")
    def move(self):
        print("Write a new coordinates for point: ")
        self.xcoord=int(input())
        self.ycoord=int(input())
    def dist(self,xcoord2,ycoord2):
        print(f"Distance between ({self.xcoord};{self.ycoord}) and ({xcoord2};{ycoord2}): ", round(((self.xcoord-xcoord2)**2+(self.ycoord-ycoord2)**2)**(1/2),3),sep=' ')

a=Point(1,2)
a.show()
a.move()
a.show()
a.dist(3,4)