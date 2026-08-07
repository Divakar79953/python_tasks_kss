# Splitting Data for Parallel Processing

import numpy as np
data=np.array([3,5,78,93,7,94])
split_data=np.split(data,3)
print("Original Data:",data)
print("split Data:")
print(split_data)
