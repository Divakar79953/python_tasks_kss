# Student Marks Analysis
import numpy as np
import pandas as pd

arr=np.array([
    [89,45],
    [34,89],
    [93,94]
    ])
df=pd.DataFrame(arr,columns=["Math","Biology"])
df["Total"]=df["Math"]+df["Biology"]
highest_student=df.loc[df["Total"].idxmax()]
print("Student Marks:")
print(df)
print("\nStudent with Highest Total:")
print(highest_student)

