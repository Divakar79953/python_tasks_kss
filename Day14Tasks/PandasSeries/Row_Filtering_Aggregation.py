# Row Filtering + Aggregation

import numpy as np
import pandas as pd
arr=np.array([
    [233,465],
    [876,342],
    [93,94],
    [321,786]
    ])
df=pd.DataFrame(arr,columns=["Sales","Profit"])
filtered=df[df["Sales"]>100]
average_profit=filtered["Profit"].mean()
print("Original DataFrame:")
print(df)
print("\nFiltered DataFrame:")
print(filtered)
print("\nAverage Profit:",average_profit)
    
