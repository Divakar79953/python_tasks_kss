# Missing Data Handling

import numpy as np
import pandas as pd
arr=np.array([93,np.nan,45,np.nan,54])
S=pd.Series(arr)
mean_value=S.mean()
updated_S=S.fillna(mean_value)
print("Original Series:")
print(S)
print("\nMean Value:",mean_value)
print("\nUpdated Series:")
print(updated_S)
