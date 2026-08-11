# Conditional Discount System

prices=[100,200,300,400,500]
updated_prices=[price*0.9 if price >200 else price for price in prices]
print("Original Prices:",prices)
print("Updated Prices:",updated_prices)
