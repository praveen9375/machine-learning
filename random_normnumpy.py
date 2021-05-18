##The second array will contain 50 numbers drawn from a normal distribution with mean 2.0 and standard deviation 3.5
import numpy as np
random_norm = np.random.normal(loc = 2.0, scale = 3.5,size = (10,5))
choices = ([6,7,8,9])
choice = np.random.choice(choices, p = [0.5,0.1,0.2,0.2])
