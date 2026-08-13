#Basic DataFrame Creation from NumPy

import numpy as np
import pandas as pd

data=np.array([[93,94],[45,46],[23,22]])
df=pd.DataFrame(data,columns=["x","y"])
print("DataFrame:")
print(df)
                
