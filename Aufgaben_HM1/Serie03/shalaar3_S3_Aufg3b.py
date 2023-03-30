import numpy as np
import matplotlib.pyplot as plt


def h(x):
    tmp = (100 * pow(x, 2)) - 200 * x + 99
    return np.sqrt(tmp)


x = np.arange(1.1000000000001, 1.3, 1e-7) # 1.1 ist eine Nullstelle, daher sorgen Werte in dieser Naehe fuer eine Ausloeschung

plt.figure(1)
plt.plot(x, h(x))
plt.xlabel('x')
plt.ylabel('h(x)')
plt.grid()

# Aufgabe b

def dh(x):
    return 100 * (x - 1) / h(x)


def k(x):
    return np.abs(x * dh(x) / h(x))


plt.figure(2)
plt.semilogy(x, k(x))
plt.xlabel('x')
plt.ylabel('k(x)')
plt.grid()

plt.show()

# Aufgabe c
# Die Kondition hat bei 1.1 eine Polstelle, daher erfolgt dort eine Auslösung



exit()

