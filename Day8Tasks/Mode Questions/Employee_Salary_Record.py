# Employee Salary Record
file=open("salary.txt","w")
n=int(input("Enter number of employees:"))
for i in range(n):
    name=input("Enter employee name:")
    salary=input("Enter employee salary:")
    file.write(name+""+salary+"\n")
file.close()
print("Employee records savedsucessfully.")
7

