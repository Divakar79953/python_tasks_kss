import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os

# CONFIG - update this if your CSV has different column names
CSV_PATH = "railway_gauges.csv"
COL_YEAR = "Year"
COL_BROAD = "Broad Gauge"
COL_METRE = "Metre Gauge"
COL_NARROW = "Narrow Gauge"
COL_TOTAL = "Total"
GRAPH_DIR="graphs"
os.makedirs(GRAPH_DIR,exist_ok=True)

# SCENARIO 1: Basic Data Loading & Cleaning
print("\nSCENARIO 1: Data Loading & Cleaning ")

df = pd.read_csv(CSV_PATH)

print("First 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values before cleaning:")
print(df.isnull().sum())

df.fillna(0, inplace=True)
print("\nMissing values after cleaning:")
print(df.isnull().sum())

gauge_cols = [COL_BROAD, COL_METRE, COL_NARROW, COL_TOTAL]
for col in gauge_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

print("\nData types after conversion:")
print(df[gauge_cols].dtypes)


df["Start_Year"] = df[COL_YEAR].str.split("-").str[0].astype(int)

# SCENARIO 2: Simple Visualization - Total Track Growth
print("\nSCENARIO 2: Total Track Growth")

years = df[COL_YEAR]
totals = df[COL_TOTAL]

plt.figure(figsize=(16, 6))
plt.plot(years, totals, marker="o", color="red")
plt.suptitle("Total Railway Tracks Over Years")
plt.xlabel("Years")
plt.ylabel("Total Tracks")
plt.grid(True, alpha=0.3)

plt.xticks(
    ticks=range(0, len(years), 5),
    labels=years[::5],
    rotation=90,
    fontsize=8
)

plt.tight_layout()
plt.savefig(os.path.join(GRAPH_DIR,"s2_total_tracks_line.png"))
plt.show()

trend = "increasing" if totals.iloc[-1] > totals.iloc[0] else "decreasing"
print(f"Trend: Total railway tracks are {trend} over the observed period "
      f"(from {totals.iloc[0]} to {totals.iloc[-1]}).")

# SCENARIO 3: Filtering + Grouped Bar Chart (Post-2000)
print("\nSCENARIO 3: Modern Railway Expansion (Post-2000)")

df_modern = df[df["Start_Year"] > 2000]
gauges_modern = df_modern[[COL_BROAD, COL_METRE, COL_NARROW]]

x = np.arange(len(df_modern))
width = 0.25

plt.figure(figsize=(16, 6))
plt.bar(x - width, df_modern[COL_BROAD], width, label="Broad Gauge", color="#4C72B0")
plt.bar(x,         df_modern[COL_METRE], width, label="Metre Gauge", color="#DD8452")
plt.bar(x + width, df_modern[COL_NARROW], width, label="Narrow Gauge", color="#55A868")

plt.suptitle("Gauge-wise Railway Expansion (Post-2000)")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.xticks(x, df_modern[COL_YEAR], rotation=90, fontsize=8)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(GRAPH_DIR,"s3_post2000_bar.png"))
plt.show()

dominant_gauge = gauges_modern.sum().idxmax()
print(f"Dominant gauge in recent years: {dominant_gauge}")

# SCENARIO 4: Feature Engineering + Pie Chart
print("\nSCENARIO 4: Gauge Contribution (Pie Chart)")

gauge_totals = df[[COL_BROAD, COL_METRE, COL_NARROW]].sum()
print("Total contribution by gauge:")
print(gauge_totals)

plt.figure(figsize=(8, 8))
plt.pie(
    gauge_totals,
    labels=gauge_totals.index,
    autopct="%1.1f%%",
    colors=["#4C72B0", "#DD8452", "#55A868"],
    startangle=90,
)
plt.suptitle("Overall Gauge Contribution")
plt.tight_layout()
plt.savefig(os.path.join(GRAPH_DIR,"s4_gauge_pie.png"))
plt.show()

top_contributor = gauge_totals.idxmax()
print(f"Highest contributing gauge overall: {top_contributor}")

# SCENARIO 5: Advanced Analysis + Multiple Graphs
print("\nSCENARIO 5: Advanced Analysis")

# --- Part 1: % contribution columns ---
df["% Broad Gauge"] = (df[COL_BROAD] / df[COL_TOTAL].replace(0, np.nan)) * 100
df["% Metre Gauge"] = (df[COL_METRE] / df[COL_TOTAL].replace(0, np.nan)) * 100
df["% Narrow Gauge"] = (df[COL_NARROW] / df[COL_TOTAL].replace(0, np.nan)) * 100
df.fillna(0, inplace=True)

print("Percentage columns added:")
print(df[[COL_YEAR, "% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"]].head())

# --- Part 2: NumPy yearly growth ---
total_arr = df[COL_TOTAL].to_numpy()
yearly_growth = np.diff(total_arr)
print("\nYearly growth in total tracks:")
print(yearly_growth)

# --- Part 3a: Line graph for all gauges ---
plt.figure(figsize=(16, 6))
plt.plot(df[COL_YEAR], df[COL_BROAD], label="Broad Gauge", marker="o")
plt.plot(df[COL_YEAR], df[COL_METRE], label="Metre Gauge", marker="o")
plt.plot(df[COL_YEAR], df[COL_NARROW], label="Narrow Gauge", marker="o")
plt.suptitle("Gauge-wise Trend Over Years")
plt.xlabel("Years")
plt.ylabel("Track Length")
plt.legend()
plt.grid(True, alpha=0.3)

plt.xticks(
    ticks=range(0, len(df[COL_YEAR]), 5),
    labels=df[COL_YEAR][::5],
    rotation=90,
    fontsize=8
)

plt.tight_layout()
plt.savefig(os.path.join(GRAPH_DIR,"s5_all_gauge_line.png"))
plt.show()

# --- Part 3b: Stacked bar chart ---
plt.figure(figsize=(16, 6))
plt.bar(df[COL_YEAR], df[COL_BROAD], label="Broad Gauge", color="#4C72B0")
plt.bar(df[COL_YEAR], df[COL_METRE], bottom=df[COL_BROAD],
        label="Metre Gauge", color="#DD8452")
plt.bar(df[COL_YEAR], df[COL_NARROW],
        bottom=df[COL_BROAD] + df[COL_METRE],
        label="Narrow Gauge", color="#55A868")
plt.title("Gauge Composition Over Years (Stacked)")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend()

plt.xticks(
    ticks=range(0, len(df[COL_YEAR]), 5),
    labels=df[COL_YEAR][::5],
    rotation=90,
    fontsize=8
)

plt.tight_layout()
plt.savefig(os.path.join(GRAPH_DIR,"s5_gauge_composition_stacked.png"))
plt.show()

# --- Part 4: Highlight growth / decline ---
max_growth_idx = np.argmax(yearly_growth)
min_growth_idx = np.argmin(yearly_growth)
print(f"\nHighest growth year: {df[COL_YEAR].iloc[max_growth_idx + 1]} "
      f"(+{yearly_growth[max_growth_idx]})")
print(f"Lowest/most negative growth year: {df[COL_YEAR].iloc[min_growth_idx + 1]} "
      f"({yearly_growth[min_growth_idx]})")

for col, name in [(COL_BROAD, "Broad Gauge"), (COL_METRE, "Metre Gauge"),
                   (COL_NARROW, "Narrow Gauge")]:
    diffs = np.diff(df[col].to_numpy())
    if (diffs < 0).any():
        decline_years = df[COL_YEAR].iloc[1:][diffs < 0].tolist()
        print(f"{name} declined in: {decline_years}")

# --- Part 5: Final conclusion ---
final_shares = df[["% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"]].iloc[-1]
leading_gauge = final_shares.idxmax()
print(f"\nCONCLUSION: In the most recent year, {leading_gauge} accounts for "
      f"{final_shares.max():.1f}% of total tracks, "
      f"{'indicating a shift toward a single dominant gauge.' if final_shares.max() > 60 else 'indicating no single gauge dominates yet.'}")

print(f"\nAll 5 graphs saved inside the '{GRAPH_DIR}' folder:")   
for fname in sorted(os.listdir(GRAPH_DIR)):                        
    print(f"  - {os.path.join(GRAPH_DIR, fname)}")                 
