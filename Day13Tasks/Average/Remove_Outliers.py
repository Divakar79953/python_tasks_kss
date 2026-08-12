# Remove Outliers

import numpy as np
values=np.array([23,45,93,94,56,67])
mean=np.mean(values)
std=np.std(values)
filtered_values=values[np.abs(values-mean)<=2*std]
print("Original Values:",values)
print("Mean:",mean)
print("Standard Deviation:",std)
print("Values Without Outliers:",filtered_values)
