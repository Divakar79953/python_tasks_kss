# Combine Two Sensor Readings

import numpy as np
sensor1=np.array([12,23,45])
sensor2=np.array([93,94,87])
combined_array=np.concatenate((sensor1,sensor2))
print("Sensor 1:",sensor1)
print("Sensor 2:",sensor2)
print("Combined Array:",combined_array)
