import numpy as np

data = [12, 6, 7, 90, 93, 94]

data_array = np.array(data)

sorted_array = np.sort(data_array)

split_array = np.split(sorted_array, 2)

sum_part1 = np.sum(split_array[0])
sum_part2 = np.sum(split_array[1])

print("Sorted Array:", sorted_array)
print("First Split Array:", split_array[0])
print("Second Split Array:", split_array[1])
print("Sum of First Part:", sum_part1)
print("Sum of Second Part:", sum_part2)
