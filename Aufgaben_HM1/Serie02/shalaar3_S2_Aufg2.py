import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return pow(x, 7) - 14 * pow(x, 6) + 84 * pow(x, 5) - 280 * pow(x, 4) + 560 * pow(x, 3) - 672 * pow(x, 2) + 448 * x - 128


def f2(x):
    return (x - 2) ** 7


# a)
x_a = np.linspace(1.99, 2.01, 501)
y1 = f1(x_a)
y2 = f2(x_a)

plt.figure(1)
plt.plot(x_a, y1, color='r')
plt.plot(x_a, y2, color='b')
plt.grid(b=True)

plt.ylim([-1e-16, 1e-16])
plt.xlabel("x")
plt.ylabel("y")

plt.legend(("f1(x)", "f2(x)"))
plt.title("Aufgabe A2 a")


# b)
def g(x):
    return x / (np.sin(1 + x) - np.sin(1))


plt.figure(2)
x_b = np.linspace(-1e-14, 1e-14, 2001)
plt.plot(x_b, g(x_b), color='g')
plt.grid()

plt.xlabel("x")
plt.ylabel("y")

plt.legend(["g(x)"])
plt.title("Aufgabe A2 b")


# c)
def g2(x):
    return x / (2 * np.cos(1 + x / 2) * np.sin(x / 2))


plt.figure(3)
x_c = np.linspace(-1e-14, 1e14, 2001)
plt.plot(x_c, g2(x_c), color='y')
plt.grid()

plt.xlabel("x")
plt.ylabel("y")

plt.title("Aufgabe A2 c")

plt.show()
