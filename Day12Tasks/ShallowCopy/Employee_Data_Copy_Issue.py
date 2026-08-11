# Employee Data Copy Issue

import copy
employees=[[101,"A",],102,"B",103,"C"]
shallow_copy=copy.copy(employees)
employees[0][1]="Z"
print("Original Employees:",employees)
print("Shallow Copy:",shallow_copy)

employees=[[101,"A",102,"B",103,"C"]]
deep_copy=copy.deepcopy(employees)
employees[0][1]="Z"
print("Original Employees:",employees)
print("Deep Copy:",deep_copy)
