# University Staff Management (Hierarchical Inheritance)

class Staff:
    def __init__(self,name):
        self.name=name

class Professor(Staff):
    def display(self):
        print("Professor Name:",self.name)

class LabAssistant(Staff):
    def display(self):
        print("Lab Assistant Name:",self.name)

class Adminstrator(Staff):
    def display(self):
        print("Adminstrator Name:",self.name)

p=Professor("Dr.Divakar")
l=LabAssistant("Rahul")
a=Adminstrator("Pooja Madhuri")

p.display()
l.display()
a.display()               
               

