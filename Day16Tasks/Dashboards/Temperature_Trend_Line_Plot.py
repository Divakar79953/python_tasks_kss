# Temperature Trend Line Plot

import matplotlib.pyplot as plt
temps=[28,34,22,29,42]
plt.plot(temps)
plt.xlabel("Days")
plt.ylabel("Temperature (C)")
plt.title("Temperature Trend")

plt.grid()
plt.show()
