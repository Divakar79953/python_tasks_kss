#Fruit Sales Comparison

import pandas as pd
s1=pd.Series([12,34,56],index=["apple","banana","cherry"])
s2=pd.Series([2,56,78],index=["apple","banana","cherry"])
total_sales=s1+s2
total=total_sales.sum()
print("Sales of Each Fruit:")
print(total_sales)
print("Total Sales:",total)
