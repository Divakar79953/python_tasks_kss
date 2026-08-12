# Accessing Specific Data

import pandas as pd
S=pd.Series([345,567,234,700,590,345,456],index=["D","I","V","A","K","A","R"])
subset=S[["I","K"]]
print("Original Series:")
print(S)
print("Subset:")
print(subset)
