# Online Shopping System (Multilevel Inheritance)

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class ElectronicProduct(Product):
    def display_product(self):
        print("Product Name:",self.name)
        print("Product Price:",self.price)

class MobilePhone(ElectronicProduct):
    def display_mobile(self):
        self.display_product()

name=input("Enter Mobile Name:")
price=int(input("Enter Mobile Price:"))

m=MobilePhone(name,price)
m.display_mobile()
