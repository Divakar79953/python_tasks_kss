#Multi-Department Data Aggregation

import numpy as np
branch_a=np.array([
    [34,87],
    [90,67]
    ])
branch_b=np.array([
    [56,78],
    [3,23]
    ])
combined_matrix=branch_a+branch_b
total_employees=np.sum(combined_matrix)
print("Combined Matrix:")
print(combined_matrix)
print("Total Employees:",total_employees)
