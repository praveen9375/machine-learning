#The final array will be a multi-dimensional array, specifically a 2-D matrix. 
#The 2-D matrix will have the integers 1, 2, 3 in its first row, and the integers 4, 5, 6 in its second row. We'll also manually set its type to np.float32.
import numpy as np
matrix = np.array([[1, 2, 3],[4, 5, 6]], dtype = np.float32)
print(repr(matrix))
