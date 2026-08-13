# Replace Values Using NumPy + Pandas
import numpy as np
import pandas as pd

S=pd.Series([23,45,67,78,91])
updated_S=np.where(S>45,0,S)
updated_S=pd.Series(updated_S)
print("Original Series:")
print(S)
print("\nUpdated Series:")
print(updated_S)
