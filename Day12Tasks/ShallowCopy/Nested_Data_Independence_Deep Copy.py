# Nested Data Independence (Deep Copy)

import copy
classes=[["Math",[30,35]],["Social",[25,45]]]
classes_copy=copy.deepcopy(classes)
classes[0][1][0]=50
print("Original Classes:",classes)
print("Copied Classes:",classes_copy)
      
