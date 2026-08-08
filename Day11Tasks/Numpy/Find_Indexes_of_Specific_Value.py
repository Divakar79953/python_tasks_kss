# Find Indexes of Specific Value

import numpy as np

defect_codes = [2, 4, 1, 4, 3, 4, 5]

codes_array = np.array(defect_codes)

indexes = np.where(codes_array == 4)

print("Indexes of 4:", indexes[0])
