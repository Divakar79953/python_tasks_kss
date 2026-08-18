import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv("Railway_Gauges.csv")

# Filter for years after 2000

df["StartYear"]=df["Year"].str.split("-").str[0].astype(int)
recent=df[df["StartYear"]>2000]

#Select Broad Gauge,Meter Gauge, Narrow Gauge

recent_gauges=recent[["Year","Broad Gauge","Metre Gauge","Narrow Gauge"]]

# Group bar chart

ax=recent_gauges.plot(x="Year",kind="bar",figsize=(12,6))
plt.xticks(rotation=90)

#Legend and labels
plt.legend(title="Gauge Type")
plt.xlabel("Year")
plt.ylabel("Number of Tracks")
plt.title("Gauge Comparison:Years After 2000")
plt.tight_layout()
plt.savefig("graphs/gauge_comparison")
plt.show()
#Which gauge dominates in recent years
total=recent_gauges[["Broad Gauge","Metre Gauge","Narrow Gauge"]]
print("Sum per gauge (post-2000):")
print(total)
print("\nDominant gauge:",total.idxmax())
