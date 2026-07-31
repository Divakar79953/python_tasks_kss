# Employee Salary System (Simple Inheritance)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def display(self):
        print("Employee Name:",self.name)
        print("Employee Salary:",self.salary)

name=input("Enter employee name:")
salary=int(input("Enter employeee salary:"))

m=Manager(name,salary)
m.display
