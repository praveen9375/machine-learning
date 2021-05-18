#Next we want to get a flattened version of the reshaped array (the flattened version is equivalent to arr), as well as a transposed version. 
#For the transposed version of reshaped, we use a permutation of (1, 2, 0).
import numpy as np
arr = np.arange(12)
reshaped = np.reshape(arr,(2,3,2))
#flattene = arr.flatten()
flattened = reshaped.flatten()
transposed = np.transpose(reshaped, axes=(1,2,0))
