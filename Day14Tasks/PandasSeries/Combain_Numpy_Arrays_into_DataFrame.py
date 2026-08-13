# Combine NumPy Arrays into DataFrame

import numpy as np
import pandas as pd

names=np.array(["D","I","V","A","K","A","R"])
marks=np.array([70,64,89,93,94,99,89])
df=pd.DataFrame({
    "Name":names,
    "Marks":marks
    })
filtered=df[df["Marks"]>60]
print("Student Data:")
print(df)
print("\nStudent with Marks Above 75:")
print(filtered)
               
