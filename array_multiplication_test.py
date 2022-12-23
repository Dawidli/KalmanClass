import numpy as np

x = np.array([2, 3, 4])
x2 = x.reshape(3, 1)
ones = np.ones(len(x)**2)
ones = ones.reshape(len(x), len(x))
print(x)




