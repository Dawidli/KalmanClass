import numpy as np


class kalman_filter:
    def __init__(self, sensor_variance: list) -> None:
        self._size = len(sensor_variance)
        self._x = np.zeros(self._size).reshape(self._size, 1)
        self._P = np.eye(self._size)
        self._variance = sensor_variance

    def predict(self, A: np.array, Q: np.array) -> None:
        new_x = A.dot(self._x)
        new_P = A.dot(self._P).dot(A.T) + Q
        self._P = new_P
        self._x = new_x

    def update(self, sensor_values: list):
        size = self._size
        for i in range(size):
            H = np.zeros(size).reshape(1, size)
            H[0][i] = 1
            z = np.array([sensor_values[i]])
            R = np.array([self._variance[i]])
            y = z - H.dot(self._x)
            S = H.dot(self._P).dot(H.T) + R

            K = self._P.dot(H.T).dot(S)
            new_x = self._x + K * y
            new_P = (np.eye(size) - K * H) * self._P

            self._P = new_P
            self._x = new_x

    @property
    def state(self) -> np.array:
        return self._x

    def prop(self) -> np.array:
        return self._P
