import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv("Railway_Gauges.csv")

gauge_totals=df[["Broad Gauge","Metre Gauge","Narrow Gauge"]].sum()

# New structure (Series) for totals
print("Total per gauge (all years):")
print(gauge_totals)

# pie chart
plt.figure(figsize=(6,6))
plt.pie(
    gauge_totals,
    labels=gauge_totals.index,
    autopct="1%.1f%%",
    startangle=90
    )
plt.title("Overall Gauge Contribution (All Years)")
plt.tight_layout()

plt.savefig("graphs/gauge")
plt.show()

print("\nDominant gauge oveerall:",gauge_totals.idxmax())
    
