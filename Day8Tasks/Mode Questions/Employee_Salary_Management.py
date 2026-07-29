# Employee Salary Management System
file=open("employees.txt","r")
highest_salary=0
highest_employee=""
print("Employee Details:")
for line in file:
    print(line.strip())
    data=line.split()
    name=data[0]
    salary=int(data[1])
    if salary>highest_salary:
        highest_salary=salary
        highest_employee=name
file.close()
print("\nHighest Salary Employee:")
print(highest_employee,"",highest_salary)
file=open("employees.txt","a")
name=input("Enter new employee name:")
salary=input("Enter employee salary:")
file.write(name+""+salary+"\n")
file.close()
print("New employee record added sucessfully.")
