# Temperature Alert System

import numpy as np
temps=np.array([23,45,34,23,43,28,32,41])
indices=np.where(temps>30)
print("Temperatures:",temps)
print("Indices:",indices[0])
