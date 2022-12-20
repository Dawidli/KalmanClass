import numpy as np

std_pos = 91.6/200
std_acc = 0.22/200

class kalman_filter():
    def __init__(self, init_x: float, x_variance: float) -> None:

        self._x = np.array([init_x])
        self._x_variance = x_variance
        self._P = np.eye(1)
        pass

    def predict(self, dt: float) -> None:
        A = np.array([1])
        new_x = A.dot(self._x)

        Q = np.array([std_pos**2])
        new_P = A.dot(self._P).dot(A.T) + Q

        self._P = new_P
        self._x = new_x

    def update(self, input_1: float, input_1_variance: float):
        self._x.reshape((1, 1))

        for i in range(1):
            pass
        pass

