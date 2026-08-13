# Multi-Line Graph for Sales Comparison

import matplotlib.pyplot as plt
data={
    "Month":["May","Oct","Sep"],
    "Store_A":[56,89,93],
    "Store_B":[94,76,88]
    }
plt.plot(data["Month"],data["Store_A"],label="Store A")
plt.plot(data["Month"],data["Store_B"],label="Store B")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.suptitle("Sales Comparision")

plt.legend()
plt.show()
