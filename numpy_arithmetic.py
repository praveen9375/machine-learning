#We'll create a couple of matrix arrays to perform our math operations on. Next we'll apply some arithmetic to arr. Specifically, we'll do multiplication, addition, and squaring.
import numpy as np
arr = np.array([[-0.5,0.8,-0.1],[0.0,-1.2,1.3]])
arr2 = np.array([[1.2,3.1],[1.2,0.3],[1.5,2.2]])
multiplied = arr*np.pi
added = arr + multiplied
Squared = added**2
