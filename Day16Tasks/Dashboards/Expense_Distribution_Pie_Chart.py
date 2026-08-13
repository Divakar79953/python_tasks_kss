# Expense Distribution Pie Chart

import matplotlib.pyplot as plt
expenses=[2000,4500,9394]
labels=["Food","Rent","Travel"]
plt.pie(expenses,labels=labels,autopct="%1.1f%%")
plt.suptitle("Monthly Expenses Distribution")
plt.show()
