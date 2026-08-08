# Convert Float Prices to Integer

import numpy as np
prices=[67,56,34,93,94]
prices_array=np.array(prices)
integer_prices=prices_array.astype(int)
print("Original Prices:",prices_array)
print("Interger prices:",integer_prices)
