import numpy as np

x = np.array([2, 3, 4])

Q = np.array([[x[0]**2,  x[0]*x[1], x[0]*x[2]],
             [x[0]*x[1], x[1]**2,   x[1]*x[2]],
             [x[0]*x[2], x[2]*x[1], x[2]**2]])
Q2 = np.cov(x)
print(Q, Q2)

