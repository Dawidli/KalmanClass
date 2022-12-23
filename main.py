import numpy as np
from include.kalman_filter import kalman_filter
import random
import time
import matplotlib.pyplot as plt

predicted_x = []
predicted_v = []
measured_x = []
measured_v = []
previous_time = 0
sensor_values = [1.0, 0.4, 0.1]
standard_deviation = [0.1, 0.1, 0.1]
kf = kalman_filter(sensor_variance=standard_deviation)


def estimate(sens_val: list, std_dev: list):
    global previous_time
    current_time = time.perf_counter()
    dt = current_time - previous_time
    previous_time = current_time
    A = np.array([[1, dt, dt ** 2 / 2],
                  [0, 1, dt],
                  [0, 0, 1]])
    Q = np.array([[std_dev[0] ** 2, std_dev[0] * std_dev[1], std_dev[0] * std_dev[2]],
                  [std_dev[1] * std_dev[0], std_dev[1] ** 2, std_dev[1] * std_dev[2]],
                  [std_dev[2] * std_dev[0], std_dev[2] * std_dev[1], std_dev[2] ** 2]])

    kf.predict(A=A, Q=Q)
    kf.update(sensor_values=sens_val)

    estimates = kf.state
    return estimates


if __name__ == "__main__":
    for i in range(500):
        test_sens_pos = random.triangular(1, 4) if i < 250 else random.triangular(4, 6)
        test_sens_vel = random.triangular(1, 2) if i < 250 else random.triangular(3, 4)
        test_sens_acc = random.triangular(0.7, 1.3) if i < 250 else random.triangular(1.3, 1.6)
        sensor_values[0] = test_sens_pos
        sensor_values[1] = test_sens_vel
        sensor_values[2] = test_sens_acc

        prediction = estimate(sens_val=sensor_values, std_dev=standard_deviation)
        if i > 3:
            predicted_x.append(prediction[0])
            predicted_v.append(prediction[1])
            measured_x.append(sensor_values[0])
            measured_v.append(sensor_values[1])

    plt.close(0)
    plt.figure(0)
    plt.plot(measured_x, 'b', label='Measured p')
    plt.plot(measured_v, "g", label="Measured v")
    plt.plot(predicted_x, 'r', label='Predicted x')
    plt.plot(predicted_v, 'r', label='Predicted v')
    plt.grid(True)
    plt.ylim(0, 7)
    plt.xlabel("Position")
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.show()
