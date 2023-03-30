import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 100, 1e-3)
y = 5 * 2 ** (-1 / 3) * x ** (-2 / 3)
t = np.log10(x)  # X Achse transformieren
z = np.log10(y)  # X Achse transformieren

plt.figure(0)
plt.plot(t, z)
plt.xlabel('t')
plt.ylabel('z')
plt.grid()

plt.figure(1)
plt.loglog(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

g = 1e5 * (2 * np.exp(1)) ** (-x / 100)
plt.figure(2)
plt.semilogy(x, g)
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid()

h = (1e4 / (2 ** 10)) ** x
plt.figure(3)
plt.semilogy(x, h)
plt.xlabel('x')
plt.ylabel('h(x)')
plt.grid()

plt.show()

exit()
