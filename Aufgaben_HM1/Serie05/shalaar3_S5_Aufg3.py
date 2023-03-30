import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def calc(f, x_0, x_1, tol):
    while f(x_1 - tol) * f(x_1 + tol) >= 0:
        x_2 = x_1 - ((x_1 - x_0) / (f(x_1) - f(x_0))) * f(x_1)
        x_0 = x_1
        x_1 = x_2
    return x_1


def f(x):
    return np.exp(pow(x, 2)) + pow(x, -3) - 10


plt.figure(1)
x_axis = np.arange(-3.5, 3.5, 0.1)

plt.plot(x_axis, f(x_axis))
plt.plot(x_axis, x_axis * 0)  # solid

plt.xlim(-3.5, 3.5)
plt.ylim(-10, 10)

plt.xlabel('x')
plt.ylabel('y')

plt.legend([
    'e^(x^2) + x^-3 -10'
    , 'Abszisse'
])
plt.title('Serie 5, A1')

plt.grid()
plt.show()

print(calc(f, -1, -1.2, 1e-5))
