import numpy as np
original_array=np.array([10,20,30,40,50,])
view_array=original_array.view()
view_array[1]=99
print("Original array after view: ",original_array)
print("View array",view_array)
copy_array=original_array.copy()
copy_array[2]=88
print("Original array after copy: ",original_array)
print("copy array",copy_array)