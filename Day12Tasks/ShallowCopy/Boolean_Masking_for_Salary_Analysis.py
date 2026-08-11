# Boolean Masking for Salary Analysis

import numpy as np
salaries=np.array([25000,45000,56000,93940])
filtered_salaries=salaries[salaries>30000]
employee_count=len(filtered_salaries)
print("Salaries Above 30000:",filtered_salaries)
print("Number of Employees:",employee_count)
