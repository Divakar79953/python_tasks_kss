# Rectangle Area Calculator

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        area=self.length*self.width
        print("Area of Rectangle:",area)

length=int(input("Enter length:"))
width=int(input("Enter width:"))

r=Rectangle(length,width)
r.area()

    
