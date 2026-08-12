# Data Alignment Issue in Series Addition

import pandas as pd
S1=pd.Series([10,20,30],index=["d","b","c"])
S2=pd.Series([5,23,15],index=["b","c","d"])
result=S1+S2
print("Additional Result:")
print(result)
result=result.fillna(0)
print("Result After Replacing NaN:")
print(result)
final_result=result.sum()
print("Final Total:",final_result)

      
             
