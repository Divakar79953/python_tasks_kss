# Reshaping Sales Data

import numpy as np

sales = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

sales_array = np.array(sales)

reshaped_sales = sales_array.reshape(4, 3)

print("Reshaped Sales:")
print(reshaped_sales)
