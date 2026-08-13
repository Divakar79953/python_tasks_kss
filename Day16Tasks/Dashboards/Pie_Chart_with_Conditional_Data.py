# Pie Chart with Conditional Data
import matplotlib.pyplot as plt
scores=[93,94,85,83,89]
pass_count=0
fail_count=0
for score in scores:
    if score > 50:
        pass_count+=1
    else:
        fail_count+=1
labels=["Pass","Fail"]
counts=[pass_count,fail_count]
plt.pie(counts,labels=labels,autopct="%1.1f%%")
plt.title("pass vs Fail")
plt.show()
