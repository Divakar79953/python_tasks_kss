# Student Marks Analysis

import numpy as np
marks=np.array([
    [56,98,78],
    [34,45,78],
    [45,67,89],
    [67,45,87]
    ])
total_marks=np.sum(marks,axis=1)
class_average=np.mean(total_marks)
students_above_average=total_marks[total_marks>class_average]
print("Total Marks of Each Student:",total_marks)
print("Class Average:",class_average)
print("Students Above Class Average:",students_above_average)
