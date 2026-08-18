import pandas as pd
from matplotlib import pyplot as plt
# Extract year and Total Columns
df=pd.read_csv("Railway_Gauges.csv")
year=df["Year"]
total=df["Total"]

# Plot a line graph showing total tracks over years

plt.figure(figsize=(10,5))
plt.plot(year,total,marker="o")
plt.xticks(rotation=70)

# Title and axis labels

plt.title("Total Railway Tracks Over Years")
plt.xlabel("Years")
plt.ylabel("Total Tracks")
plt.tight_layout()

plt.savefig("graphs/total_tracks_line.png")
plt.show()

#Identify whether the trend is increasing or decreasing

print("First year Total:",total.iloc[0])
print("Last year Total:",total.iloc[-1])
if total.iloc[-1]>total.iloc[0]:
    print("Overall trend:Increasing")
else:
    print("Overall trend:Decreasing")
                
