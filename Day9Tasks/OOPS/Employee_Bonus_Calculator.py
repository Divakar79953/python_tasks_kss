# Employee Bonus Calculator (Decorators & OOP)

def bonus(func):
    def wrapper(self):
        self.salary=self.salary+5000
        func(self)
    return wrapper

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @bonus
    def display(self):
        print("Employee Name:",self.name)
        print("Salary After Bonus:",self.salary)

name=input("Enter Employee Name:")
salary=int(input("Enter Employee Salary:"))

e=Employee(name,salary)
e.display()
 
