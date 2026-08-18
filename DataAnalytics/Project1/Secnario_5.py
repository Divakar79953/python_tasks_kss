import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('railway_gauges.csv')

#  New % 
df['% Broad Gauge'] = df['Broad Gauge'] / df['Total'] * 100
df['% Metre Gauge'] = df['Metre Gauge'] / df['Total'] * 100
df['% Narrow Gauge'] = df['Narrow Gauge'] / df['Total'] * 100

#  Yearly growth of Total using np.
total_array = df['Total'].to_numpy()
growth = np.diff(total_array)            
df['Growth'] = np.insert(growth, 0, 0)   

#  Line graph for all gauges 
plt.figure(figsize=(12, 6))
plt.plot(df['Year'], df['Broad Gauge'], label='Broad Gauge')
plt.plot(df['Year'], df['Metre Gauge'], label='Metre Gauge')
plt.plot(df['Year'], df['Narrow Gauge'], label='Narrow Gauge')
plt.xticks(rotation=70)
plt.xlabel('Year')
plt.ylabel('Number of Tracks')
plt.title('Gauge Trends Over Time')
plt.legend()
plt.tight_layout()
plt.savefig('graphs/all_gauges_line.png')
plt.show()

# Stacked bar chart of composition 
plt.figure(figsize=(14, 6))
plt.bar(df['Year'], df['Broad Gauge'], label='Broad Gauge')
plt.bar(df['Year'], df['Metre Gauge'], bottom=df['Broad Gauge'], label='Metre Gauge')
plt.bar(df['Year'], df['Narrow Gauge'],
        bottom=df['Broad Gauge'] + df['Metre Gauge'], label='Narrow Gauge')
plt.xticks(rotation=70)
plt.xlabel('Year')
plt.ylabel('Number of Tracks')
plt.title('Gauge Composition Over Time (Stacked)')
plt.legend()
plt.tight_layout()
plt.savefig('graphs/gauge_composition_stacked.png')
plt.show()

# Highlights 
max_growth_idx = df['Growth'].idxmax()
min_growth_idx = df['Growth'].idxmin()
print(f"Highest growth year: {df.loc[max_growth_idx, 'Year']} "
      f"(+{df.loc[max_growth_idx, 'Growth']} tracks)")
print(f"Biggest drop year: {df.loc[min_growth_idx, 'Year']} "
      f"({df.loc[min_growth_idx, 'Growth']} tracks)")

metre_start = df['Metre Gauge'].iloc[0]
metre_end = df['Metre Gauge'].iloc[-1]
narrow_start = df['Narrow Gauge'].iloc[0]
narrow_end = df['Narrow Gauge'].iloc[-1]
print(f"\nMetre Gauge: {metre_start} -> {metre_end} "
      f"({'decline' if metre_end < metre_start else 'growth'})")
print(f"Narrow Gauge: {narrow_start} -> {narrow_end} "
      f"({'decline' if narrow_end < narrow_start else 'growth'})")

broad_start_pct = df['% Broad Gauge'].iloc[0]
broad_end_pct = df['% Broad Gauge'].iloc[-1]
print(f"\nBroad Gauge share: {broad_start_pct:.1f}% -> {broad_end_pct:.1f}%")

#  Final conclusion
print("\nConclusion: Broad Gauge's share has risen sharply while Metre Gauge's "
      "share has collapsed and Narrow Gauge stayed marginal throughout - "
      "yes, the railway system is shifting toward a single dominant gauge (Broad Gauge).")
