# Accessing Matrix Data

import numpy as np
marks=[[78,98],
       [77,98],
       [45,34],
       [23,87],
       [93,94]]
marks_array=np.array(marks)
print("Second student's second subject marks:",marks_array[1,1])
