# Filter Only Passed Students

import pandas as pd
df=pd.DataFrame({
    "Name":["D","I","V","A","K","A","R"],
    "Marks":[93,94,85,89,77,49,50]
    })
df["Status"]=["Pass" if mark >= 50 else "Fail" for mark in df["Marks"]]
passed_students=df[df["Status"]=="Pass"]
print("Passed Students:")
print(passed_students)
