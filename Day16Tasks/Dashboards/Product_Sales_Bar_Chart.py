# Product Sales Bar Chart
import matplotlib.pyplot as plt

products=["Pen","Book","stationery Box"]
sales=[50,80,34]
plt.bar(products,sales)
plt.xlabel("Products")
plt.ylabel("Sales")
plt.suptitle("Product Sales")
plt.show()
