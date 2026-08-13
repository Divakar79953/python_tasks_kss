# Employee Management System

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


employees = {}

try:
    n = int(input("Enter number of employees: "))

    for i in range(n):

        name = input("Enter employee name: ")

        salary = float(input("Enter employee salary: "))

        employee = Employee(name, salary)

        employees[name] = employee

except ValueError:
    print("Invalid salary or number entered.")


print("\nEmployee Details:")

for name, employee in employees.items():
    employee.display()

with open("employees.txt", "w") as file:

    for name, employee in employees.items():
        file.write("Name: " + employee.name + "\n")
        file.write("Salary: " + str(employee.salary) + "\n")
        file.write("\n")

print("\nEmployee data saved successfully.")

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


employees = {}

try:
    n = int(input("Enter number of employees: "))

    for i in range(n):

        name = input("Enter employee name: ")

        salary = float(input("Enter employee salary: "))

        employee = Employee(name, salary)

        employees[name] = employee

except ValueError:
    print("Invalid salary or number entered.")


print("\nEmployee Details:")

for name, employee in employees.items():
    employee.display()

with open("employees.txt", "w") as file:

    for name, employee in employees.items():
        file.write("Name: " + employee.name + "\n")
        file.write("Salary: " + str(employee.salary) + "\n")
        file.write("\n")

print("\nEmployee data saved successfully.")
