import numpy as np
import matplotlib.pyplot as plt

# A)
x_data = np.array([1997, 1999, 2006, 2010]) - 1997  # subtract smallest value to shift zero
y_data = np.array([150, 104, 172, 152])

A = np.array([
    [pow(x_data[0], 3), pow(x_data[0], 2), pow(x_data[0], 1), pow(x_data[0], 0)],
    [pow(x_data[1], 3), pow(x_data[1], 2), pow(x_data[1], 1), pow(x_data[1], 0)],
    [pow(x_data[2], 3), pow(x_data[2], 2), pow(x_data[2], 1), pow(x_data[2], 0)],
    [pow(x_data[3], 3), pow(x_data[3], 2), pow(x_data[3], 1), pow(x_data[3], 0)]
])

b = np.copy(y_data).T

coeff = np.linalg.solve(A, b)
plt.figure(1)
x_graph = np.arange(0, 15, 0.01)
y_graph = np.polyval(coeff, x_graph)
plt.plot(x_data, y_data, color='r', marker='o', linestyle='', markersize='10')
plt.plot(x_graph, y_graph, color='b')
plt.ylim([0, 200])
plt.grid()

# B)
x_est = np.array([2003, 2004]) - 1997
y_est = np.polyval(coeff, x_est)
plt.plot(x_est, y_est, color='g', marker='*', linestyle='', markersize='10')

# C)
x_est2 = x_graph
y_est2 = np.polyval(np.polyfit(x_data, y_data, 3), x_est2)

plt.figure(2)
plt.grid()
plt.plot(x_est2, y_est2)

plt.show()
