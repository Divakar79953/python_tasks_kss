# Student Marks DataFrame Analysis

import pandas as pd
data=pd.DataFrame({
    "Name":["V","D","N"],
    "Math":[90,93,94],
    "Biology":[80,83,84]
    })
data["Total"]=data["Math"]+data["Biology"]
highest_student=data.loc[data["Total"].idxmax()]
print("Student Data:")
print(data)
print("Student With Highest Total:")
print(highest_student)
    
                                    
