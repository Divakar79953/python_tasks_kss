#Product Sales & Profit Analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales=np.array([200,345,500,899,2000,9394])
profit=np.array([40,60,30,50,80,70])
products=["V","N","A","I","D","U"]

df=pd.DataFrame({
    "Product":products,
    "Sales":sales,
    "Profit":profit
    })
plt.subplot(2,3,1)
plt.plot(products,sales,marker="D",label="Sales")
plt.title("Product Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)

plt.subplot(2,3,2)
plt.bar(products,sales)
plt.title("Product vs Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.subplot(2,3,3)
plt.pie(
    sales,
    labels=products,
    autopct="1%.1f%%"
    )
plt.title("Sales Contribution")

plt.subplot(2,3,4)
plt.hist(profit,bins=5)
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

plt.subplot(2,3,5)
plt.scatter(sales,profit)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)
               
plt.subplot(2,3,6)
plt.axis("off")

plt.tight_layout()
plt.show()

               
