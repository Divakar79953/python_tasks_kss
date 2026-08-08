# Filter High Temperature Values

import numpy as np

temperatures = [28, 31, 35, 27, 40, 22]

temperature_array = np.array(temperatures)

high_temperatures = temperature_array[temperature_array > 30]

print("Temperatures above 30°C:", high_temperatures)
