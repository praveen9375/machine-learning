#We'll now create our own distribution of strings and randomly select from it. The values for our distribution will be 'a', 'b', 'c', 'd'.
#To choose a value, we'll use a probability distribution of [0.5, 0.1, 0.2, 0.2], i.e. 'a' will have probability 0.5 of being chosen, 'b' will have a probability of 0.1, etc.
import numpy as np
random_uniform = np.random.uniform(low =-2.5, high = 1.5, size=(5)) 
random_norm = np.random.normal(loc = 2.0, scale = 3.5,size = (10,5))
choices = ([6,7,8,9])
choice = np.random.choice(choices, p = [0.5,0.1,0.2,0.2])
arr = np.array([1,2,3,4,5])
np.random.shuffle(arr)
