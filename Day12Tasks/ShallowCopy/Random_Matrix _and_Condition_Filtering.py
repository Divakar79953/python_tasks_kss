# Random Matrix and Condition Filtering

import numpy as np
matrix=np.random.randint(0,34,(7,7))
filtered_values=matrix[matrix>25]
print("Random Matrix:")
print(matrix)
print("Values Greater Than 25:")
print(filtered_values)
