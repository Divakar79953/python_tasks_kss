# Missing City Data
import pandas as pd
cities={
    "Amaravathi":700000,
    "Hyderabad":500000,
    "Mumbai":300000
    }
city_data=pd.Series(cities,index=["Amaravathi","Hyderabad","Chennai"])
missing_cities=city_data[city_data.isna()]
print("City Data:")
print(city_data)
print("Missing Cities:")
print(missing_cities)

                    
