#The final array will contain 101 evenly spaced numbers between -3.5 and 1.5, inclusive. Since they are evenly spaced, the difference between adjacent numbers is 0.05.
import numpy as np
points = np.linspace(-3.5, 1.5, num = 101)
print(repr(points))
