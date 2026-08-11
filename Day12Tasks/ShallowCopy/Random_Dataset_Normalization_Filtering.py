# Random Dataset Normalization + Filtering

import numpy as np
data=np.random.rand(7)
normalized_data=data*100
filtered_data=normalized_data[normalized_data>50]
sorted_data=np.sort(filtered_data)
print("Original Data:",data)
print("Normalized Data:",normalized_data)
print("Filtered Data:",filtered_data)
print("Sorted Data:",sorted_data)
