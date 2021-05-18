#The next two arrays will use floating point numbers. The first array will be upcast to floating point numbers, while we manually cast the second array using np.float32.
#For manual casting, we use an array's inherent astype function, which takes in the new type as an argument and returns the casted array.
import numpy as np
float_arr = ([1,5.4,3])
float_arr2 = arr2.astype(np.int32)
print(repr(float_arr))
print(repr(float_arr2))
