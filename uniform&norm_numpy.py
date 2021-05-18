#The next two arrays will be drawn randomly from distributions. The first will contain 5 numbers drawn uniformly from the range [-2.5, 1.5].
import numpy as np
random_uniform = np.random.uniform(low =-2.5, high = 1.5, size=(5)) 
random_norm = np.random.normal(loc = 2.0, scale = 3.5,size = (10,5))
