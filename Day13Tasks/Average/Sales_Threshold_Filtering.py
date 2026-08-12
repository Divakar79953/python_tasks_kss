# Sales Threshold Filtering

import numpy as np
sales=np.array([93940,23400,67899,45798])
average_sales=np.mean(sales)
filtered_sales=sales[sales>average_sales]
print("Average Sales:",average_sales)
print("Sales Above Average:",filtered_sales)
