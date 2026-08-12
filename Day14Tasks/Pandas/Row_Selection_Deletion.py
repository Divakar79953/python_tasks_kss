# Row Selection & Deletion

import pandas as pd
df=pd.DataFrame({
    "D":[10,20,30],
    "I":[4,56,45]
    },index=["x","y","z"])
row_y=df.loc["y"]
print("Row y:")
df=df.drop("x")
print("Updated DataFrame:")
print(df)
