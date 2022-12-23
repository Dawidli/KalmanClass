import numpy as np
a = 1
A = np.eye(3)*2
B = np.eye(3)*3
A2 = np.zeros(3).reshape(3, 1)
C = np.eye(3)
AA = [1,2,3,4,5,6,6,7,8]
x = np.ones(9).reshape(3, 3) * np.array([[1, 0, 0],
                                         [0, 0, 0]]) * np.array([[1],
                                                                [0],
                                                                [0]])
AB = A.dot(B).astype(int)

print(x)

