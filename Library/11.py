import numpy as np
arrayy=np.shape([[1,2,3],[4,5,6]])
print("Elements:")
for element in np.nditer(arrayy):
    print(element)