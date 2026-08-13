# Find Maximum Value

import numpy as np
import pandas as pd
arr=np.array([12,45,87,34])
S=pd.Series(arr)
maximum=S.max()
print("Series:")
print(S)
print("Maximum Value:",maximum)
