# Reshape & Row Averages

import numpy as np
data=np.arange(1,13)
matrix=data.reshape(3,4)
row_average=np.mean(matrix,axis=1)
print("3*4 Matrix:")
print(matrix)
print("Row Averages:",row_average)
