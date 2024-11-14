import numpy as np
unsorted=np.array([14,12,5,23,89,1])
sorted=np.sort(unsorted)
print("Sprted array:",sorted)
value=23
index=np.where(sorted==value)
if index[0].size>0:
    print(f"{value} found at index {index[0][0]}")
else:
    print(f"{value} not found in the array")