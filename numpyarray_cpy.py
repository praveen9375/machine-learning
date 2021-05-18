#We now want to copy the array so we can change the first element to 10. This way we don't modify the original array.
import numpy as np
arr2 = arr.copy()
arr2[0] = 10
arr = np.array([np.nan,2,3,4,5])
print(repr(arr))
print(repr(arr2))
