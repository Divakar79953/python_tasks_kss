#Combined Visualization Dashboard

import matplotlib.pyplot as plt
sales=[450,340,250,550,630]
products=["N","A","I","D","U"]
plt.figure(figsize=(10,6))
plt.subplot(1,3,1)
plt.plot(products,sales)
plt.title("Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.subplot(1,3,2)
plt.bar(products,sales)
plt.title("Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.subplot(1,3,3)
plt.pie(sales,labels=products,autopct="%1.1f%%")
plt.title("Sales Distribution")
plt.tight_layout()
plt.show()
