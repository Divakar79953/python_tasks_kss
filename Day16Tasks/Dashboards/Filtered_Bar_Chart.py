# Filtered Bar Chart

import matplotlib.pyplot as plt
marks=[45,50,67,89,90,93,94]
names=["D","I","V","A","K","A","R"]
filtered_names=[]
filtered_marks=[]
for i in range(len(marks)):
    if marks[i]>50:
        filtered_names.append(names[i])
        filtered_marks.append(marks[i])
plt.bar(filtered_names,filtered_marks)
plt.xlabel("Students Names")
plt.ylabel("Marks")
plt.suptitle("Student with Marks above 50")

plt.show()

    
