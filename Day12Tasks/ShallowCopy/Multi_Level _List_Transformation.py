# Multi-Level List Transformation

data=[[1,2,3],[4,8],[7]]
flat_data=[num for sublist in data for num in sublist]
even_squares=[num**2 for num in flat_data if num %2==0]
print("Flattened List:",flat_data)
print("Squares of Even Numbers:",even_squares)
