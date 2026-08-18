import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv("railway_gauges.csv")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())
print("\ncolumn names:",list(df.columns))

print("\nMissing values per column:")
print(df.isnull().sum())

df=df.fillna(0)

gauge_cols=["Broad Gauge","Metre Gauge","Total"]
for col in gauge_cols:
    df[col]=pd.to_numeric(df[col],errors="coerce")

print("\nData types after converion:")
print(df.dtypes)

plot_df=df.drop("Total",axis=1)
ax=plot_df.plot(x="Year",kind="bar",figsize=(14,6))
plt.xticks(rotation=70)
plt.xlabel("Year")
plt.ylabel("Number of Tracks")
plt.suptitle("Railway Gauges:Tracks Installed per year")
plt.tight_layout()
plt.savefig("graphs/scenario1_bar.png")
plt.show()
                
