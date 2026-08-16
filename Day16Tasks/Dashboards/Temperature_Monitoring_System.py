#Temperature Monitoring System
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps=np.array([33,32,28,40,35,29,30])
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

df=pd.DataFrame({
    "Day":days,
    "Temperature":temps
    })
print("Temperature Data:")
print(df)

high_count=np.sum(temps > 30)
low_count=np.sum(temps <= 30)

plt.subplot(2,3,1)
plt.plot(days,temps,marker="o",label="Temperature")
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.legend()
plt.grid(True)

plt.subplot(2,3,2)
plt.bar(days,temps)
plt.title("Day-wise Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")

plt.subplot(2,3,3)
plt.pie([high_count,low_count],
        labels=["High","Low"],
        autopct="%1.1f%%"
        )
plt.title("High vs Low Temperature")

plt.subplot(2,3,4)
plt.hist(temps,bins=5)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")

plt.subplot(2,3,5)
plt.scatter(range(len(temps)),temps)
plt.title("Day Index vs Temperature")
plt.xlabel("Day Index")
plt.ylabel("Temperature")
plt.grid(True)

plt.tight_layout()
plt.show()

