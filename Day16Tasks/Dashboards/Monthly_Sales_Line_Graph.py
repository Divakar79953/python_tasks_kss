# Monthly Sales Line Graph

import matplotlib.pyplot as plt
sales=[100,200,300,400,700]
months=["Jan","Feb","Mar","Apr","May"]
plt.plot(months,sales)

plt.xlabel("Months")
plt.ylabel("Sales")
plt.suptitle("Monthly Sales")
plt.show()
        
