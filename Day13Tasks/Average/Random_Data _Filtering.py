# Random Data & Filtering
import numpy as np
nums=np.random.randint(1,100,20)
filtered_nums=nums[nums%5==0]
sorted_nums=np.sort(filtered_nums)
print("Random Numbers:",nums)
print("Numbers Divisible by 5:",sorted_nums)
