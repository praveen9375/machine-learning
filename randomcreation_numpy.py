#We'll start off by obtaining some random integers. The first integer we get will be randomly chosen from the range [0, 5). 
#The remaining integers will be part of a 3x5 NumPy array, each randomly chosen from the range [3, 10).
import numpy as np
random1 = np.random.randint(5)
random_arr = np.random.randint(3, high = 10, size=(3,5))
