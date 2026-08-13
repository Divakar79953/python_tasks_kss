# Data Cleaning  Visualization
import matplotlib.pyplot as plt

data = [150, None, 450, 160, None, 300]

valid_values = [value for value in data if value is not None]

average = sum(valid_values) / len(valid_values)

cleaned_data = []

for value in data:
    if value is None:
        cleaned_data.append(average)
    else:
        cleaned_data.append(value)
above_average = []

for value in cleaned_data:
    if value > average:
        above_average.append(value)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(cleaned_data)
plt.title("Cleaned Data - Line Graph")
plt.xlabel("Index")
plt.ylabel("Value")

plt.subplot(1, 2, 2)
plt.bar(range(len(above_average)), above_average)
plt.title("Values Above Average")
plt.xlabel("Index")
plt.ylabel("Value")

plt.tight_layout()
plt.show()
