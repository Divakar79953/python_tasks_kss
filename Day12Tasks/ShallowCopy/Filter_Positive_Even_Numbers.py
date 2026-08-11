# Filter Positive Even Numbers

import numpy as np
arr=[-3,-5,-6,10,12,20,45,93,94]
arr_array=np.array(arr)
filtered_values=arr_array[(arr_array>0)&(arr_array %2==0)]
print("Original Array:",arr_array)
print("Positive Even Numbers:",filtered_values)
