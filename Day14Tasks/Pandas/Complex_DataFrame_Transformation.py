# Complex DataFrame Transformation

import pandas as pd
df=pd.DataFrame({
    "Name":["D","I","V","A","K","A","R"],
    "Marks":[93,94,56,65,78,34,97]
    })
df["Status"]=["Pass" if mark >= 50 else "Fail" for mark in df["Marks"]]
passed_students=df[df["Status"]=="Pass"]
average_marks=passed_students["Marks"].mean()
print("Complete DataFrame:")
print(df)
print("\nPassed Students:")
print(passed_students)
print("\nAverage Marks of Passed Students:",average_marks)
