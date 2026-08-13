# Student Marks Bar Chart

import matplotlib.pyplot as plt

names=["D","I","V","A","K","A","R","N","A","I","D","U"]
marks=[93,89,78,85,78,87,94,68,85,93,94,99]
plt.bar(names,marks)
plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.suptitle("Student Marks")
plt.show()
