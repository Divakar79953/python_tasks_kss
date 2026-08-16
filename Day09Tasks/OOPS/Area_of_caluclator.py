# Area of Calculator

class Circle:
    def __init__(self,radius):
        self.radius=radius        

    def area(self):
        print("Area of Circle:",3.14*self.radius*self.radius) # pie*r square or pie*r*r


class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("Area of Rectangle:",self.length*self.breadth)  #l*b

class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        print("Area of Triangle:",0.5*self.base*self.height) # 1/2*b*h


circle=Circle(7)
rectangle=Rectangle(7,9)
triangle=Triangle(3,5)

circle.area()
rectangle.area()
triangle.area()

    
