import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    # Without fancy methods
    # return x ** 5 - 5 * x ** 4 - 30 * x ** 3 + 110 * x ** 2 + 29 * x ** 1 - 105 * x ** 0

    # With fancy methods
    return pow(x, 5) - 5 * pow(x, 4) - 30 * pow(x, 3) + 110 * pow(x, 2) + 29 * x - 105


def df1(x):
    # Without fancy methods
    return 5 * pow(x, 4) - 4 * 5 * pow(x, 3) - 3 * 30 * pow(x, 2) + 2 * 110 * pow(x, 1) + 1 * 29 * pow(x, 0) - 0 * 105 * pow(x, -1)

    # With fancy methods TODO: Refer https://stackoverflow.com/questions/9876290/how-do-i-compute-derivative-using-numpy
    # return np.poly1d(x)


def F1(x):
    # Without fancy methods
    return pow(x, 6) / 6 - pow(x, 5) - 15 * pow(x, 4) / 2 + 110 * pow(x, 3) / 3 + 29 * pow(x, 2) / 2 - 105 * x

    # With fancy methods TODO: Refer
    # return np.poly1d(x)


x_axis = np.arange(-10, 10, 0.1)
f = f1(x_axis)
df = df1(x_axis)
F = F1(x_axis)
plt.plot(x_axis, f)
plt.plot(x_axis, df)
plt.plot(x_axis, F)

plt.xlim(-10, 10)
plt.ylim(-1300, 1300)

plt.xlabel('x')
plt.ylabel('y')

plt.legend(['Polynom', 'Ableitung', 'Stammfunktion'])
plt.title('Plynom, Ableitung sowie Stammfunktion A1')

plt.grid()
plt.show()

exit()
