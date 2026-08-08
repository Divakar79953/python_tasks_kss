#Copy vs View Behavior

import numpy as np

data = np.array([10, 20, 30, 40])

copy_array = data.copy()

data[0] = 100

print("Original Array:", data)
print("Copy Array:", copy_array)

view_array = data.view()

data[1] = 200

print("Original Array:", data)
print("View Array:", view_array)
