# Vehicle Management System (Inheritance)

class Vehicle:
    def __init__(self,brand,speed,specifications):
        self.brand=brand
        self.speed=speed
        self.specifications=specifications

class Car(Vehicle):
    def display(self):
       print("Car Brand:",self.brand)
       print("Car Speed:",self.speed)
       print("Car Specifications:",self.specifications)

class Bike(Vehicle):
    def display(self):
        print("Bike Brand:",self.brand)
        print("Bike Speed:",self.speed)
        print("Bike Specifications:",self.specifications)

car=Car("Defender",250,"Desiel or Petrol")
bike=Bike("Royal Enfield",45,"Petrol")

car.display()
bike.display()


        
    
