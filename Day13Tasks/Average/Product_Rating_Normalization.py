# Product Rating Normalization
import numpy as np
ratings=np.array([4,5,6,2,7,8,])
maximum=np.max(ratings)
minimum=np.min(ratings)
normalized=(ratings-minimum)/(maximum-minimum)
print("Original Ratings:",ratings)
print("Normalized Ratings:",normalized)
