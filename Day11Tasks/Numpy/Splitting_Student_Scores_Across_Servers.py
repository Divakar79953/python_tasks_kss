#Splitting Student Scores Across Servers

import numpy as np

scores = [50, 60, 70, 80, 90, 100, 110, 120]

score_array = np.array(scores)

split_scores = np.array_split(score_array, 4)

print("Split Scores:", split_scores)
