import numpy
from include.kalman_filter import kalman_filter
import random
import time
import matplotlib.pyplot as plt


kf = kalman_filter(init_x=0.0, x_variance=0.01)

predicted_v = []
measured_v = []
predicted_v = []
measured_v = []
previous_time = 0
val1 = 2
val2 = 4


def estimate(input):
    global previous_time
    current_time = time.perf_counter()
    delta = current_time - previous_time
    previous_time = current_time

    kf.predict(dt=delta)
    kf.update(input_1=input, input_1_variance=0.01)

    estimates = kf.state
    return estimates


if __name__ == "__main__":
    for i in range(500):
        test_sens = random.triangular(1, 4)
        #test_sens = val1 if (i % 2) == 0 else val2
        prediction = estimate(test_sens)

        predicted_v.append(prediction)
        measured_v.append(test_sens)

    plt.close(0); plt.figure(0)
    plt.plot(measured_v, 'b', label ='Measured')
    plt.plot(predicted_v, 'r', label ='Predicted')
    plt.ylim(1, 5)
    plt.grid(True)
    plt.xlabel("Position")
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.show()




