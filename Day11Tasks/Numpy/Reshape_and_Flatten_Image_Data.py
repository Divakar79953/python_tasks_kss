# Reshape and Flatten Image Data

import numpy as np

image = [[1, 2, 3],
         [4, 5, 6]]

image_array = np.array(image)

reshaped_image = image_array.reshape(3, 2)
flattened_image = reshaped_image.flatten()

print("Original Image:")
print(image_array)

print("Reshaped Image:")
print(reshaped_image)

print("Flattened Image:")
print(flattened_image)
