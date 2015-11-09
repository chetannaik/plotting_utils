import numpy as np
from pylab import *

data = { (3, 3): 1.7314, (3,4):-6.99, (4, 3):-17.3, (4, 4):-100.0 }
matrix = np.zeros((5, 5))
for (x, y), z in data.items():
        matrix[y,x] = z
imshow(matrix[3:, 3:], origin='lower', interpolation='none', extent=[2.5, 4.5, 2.5, 4.5])
show()
