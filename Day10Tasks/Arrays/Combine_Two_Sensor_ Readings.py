# Combine Two Sensor Readings

import numpy as np
sensor1=np.array([12,34,56])
sensor2=np.array([50,30,56)]
combined=np.concatenate((sensor1,sensor2))
print("Sensor1:",sensor1)
print("Sensor2:",sensor2)
print("Combined Array:",combined)
