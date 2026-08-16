#Employee Salary Insights

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
salaries=np.array([25000,30000,28000,50000,40000,35000])
departments=["HR","IT","HR","IT","Sales","Sales"]
df=pd.DataFrame({
    "Department":departments,
    "Salary":salaries
    })
print("Employee Salary Data:")
print(df)

plt.figure(figsize=(6,4))
plt.plot(range(len(salaries)),salaries,marker="o",label="Salary")
plt.suptitle("Employee Salary Trend")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(6,4))
plt.bar(departments,salaries)
plt.suptitle("Department-wise Salary Comparison")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()

department_count=df["department"].value_counts()
plt.figure(figsize=(5,5))
plt.pie(
    department_count,
    labels=department_count.index,
    autopct="%1.1f%%"

)
plt.suptitle("Department Distribution")
plt.show()

plt.figure(figsize=(6,4))
plt.hist(salaries,bins=5)
plt.suptitle("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(range(len(salaries)),salaries)
plt.suptitle("Index vs Salary")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.grid()
plt.show()
