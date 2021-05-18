#The first array we'll create comes straight from a list of integers and np.nan. 
#The list contains np.nan as the first element, and the integers from 2 to 5, inclusive, as the next four elements.
import numpy as np
arr = np.array([np.nan,2,3,4,5], dtype=np.float32)
print(repr(arr))
