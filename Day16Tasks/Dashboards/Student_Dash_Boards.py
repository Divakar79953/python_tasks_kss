#Student Performance Dashboard

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
marks=np.array([79,93,94,56,65,91,92])
students=["D","I","V","A","K","A","R"]
df=pd.DataFrame({
    "Student":students,
    "Marks":marks
    })
print("Student Performance Data:")
print(df)
plt.figure(figsize=(6,4))
plt.plot(students,marks,marker="o")
plt.suptitle("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

pass_count=np.sum(marks >50)
fail_count=np.sum(marks <=50)
plt.figure(figsize=(5,5))
plt.pie([pass_count,fail_count],
        labels=["Pass","Fail"],
        autopct="%1.1f%%")
plt.title("Pass vs Fail"),
plt.show()
           
plt.figure(figsize=(6,4))
plt.hist(marks,bins=5)
plt.suptitle("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(range(len(marks)),marks)
plt.suptitle("Index vs Marks")
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()
