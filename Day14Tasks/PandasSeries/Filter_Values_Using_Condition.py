# Filter Values Using Condition
import numpy as np
import pandas as pd

arr=np.array([93,94,84,83,86])
S=pd.Series(arr)
filtered=S[S>30]
print("Original Series:")
print(S)
print("Values Greater Than 30:")
print(filtered)
