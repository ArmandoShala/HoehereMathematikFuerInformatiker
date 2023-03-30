import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return pow(x, 7) - 14 * pow(x, 6) + 84 * pow(x, 5) - 280 * pow(x, 4) + 560 * pow(x, 3) - 672 * pow(x, 2) + 448 * x - 128

def f2(x):
    return (x - 2) ** 7


# def plotData(x_axis, y_axis, title, legend=[], xlabel="x", ylabel="y", xlimMin=0, xlimMax=0, ylimMin=0,
#              ylimMax=0):
#     if xlimMin != 0 and xlimMax != 0:
#         plt.xlim(xlimMin, xlimMax)
#     if ylimMin != 0 and ylimMax != 0:
#         plt.ylim(ylimMin, ylimMax)
#
#     plt.title(title)
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.plot(x_axis, y_axis)
#
#     plt.grid()
#     plt.show()


x = np.linspace(1.99, 2.01, 501)
y1 = f1(x)
y2 = f2(x)

plt.figure(1)
plt.plot(x, y1, color='r')
plt.plot(x, y2, color='b')
plt.grid(b=True)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(("f1(x)", "f2(x)"))

plt.ylim([-1e-16, 1e-16])


# plotData(x, yb, "A2b")
# plotData(x, yc, "A2c")


def g1(x):
    return x / (np.sin(1 + x) - np.sin(1))


x3 = np.linspace(-1e-14, 1e-14, 2001)
y3 = g1(x3)
plt.figure(2)
plt.xlabel("x")
plt.ylabel("y")
plt.legend("g1(x)")

plt.grid()
plt.plot(x3, y3, color='r')


# c)
# def g2(x):
#     return x / (2 * np.cos(1 + x / 2) * np.sin(x / 2))
#
#
# y4 = g2(x3)
# plt.figure(3)
# plt.plot(x3, y4)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend('g2(x)')
# plt.grid(b=True)
#

plt.show()

