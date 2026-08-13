#Data Analysis Tool

import numpy as np
import pandas as pd

marks = np.random.randint(0, 101, 5)

df = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": marks
})

average = np.mean(df["Marks"])

passed_students = df[df["Marks"] >= 50]

print("Student Marks:")
print(df)

print("\nAverage Marks:", average)

print("\nPassed Students:")
print(passed_students)

print("\nStudent Results:")

for index, row in df.iterrows():
    if row["Marks"] >= 50:
        print(row["Student"], "Pass")
    else:
        print(row["Student"], "Fail")
