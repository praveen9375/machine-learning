#Our initial array will just be all the integers from 0 to 11, inclusive. We'll also reshape it so it has three dimensions.
import numpy as np
arr = np.arange(12)
reshaped = np.reshape(arr,(2,3,2))
