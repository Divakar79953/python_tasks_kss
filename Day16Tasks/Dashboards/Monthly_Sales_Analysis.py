# Monthly Sales Analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales=np.array([250,345,950,930,940,550])
months=["Jan","Feb","Mar","Apr","May","Jun"]
df=pd.DataFrame({
    "Month":months,
    "Sales":sales
    })
print("Monthly Sales Data:")
print(df)
plt.figure(figsize=(6,4))
plt.plot(months,sales,marker="o",label="Monthly Sales")
plt.suptitle("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(6,4))
plt.bar(months,sales)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

plt.figure(figsize=(5,5))
plt.pie(sales,labels=months,
        autopct="%1.1f%%")
plt.suptitle("Monthly Sales Contribution")
plt.show()

plt.figure(figsize=(6,4))
plt.hist(sales,bins=5)
plt.suptitle("Sale Distribution")
plt.xlabel("Sale")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(range(len(sales)),sales)
plt.suptitle("Month Index vs Sales")
plt.xlabel("Month Index")
plt.ylabel("Sale")
plt.legend()
plt.grid(True)
plt.show()


        
