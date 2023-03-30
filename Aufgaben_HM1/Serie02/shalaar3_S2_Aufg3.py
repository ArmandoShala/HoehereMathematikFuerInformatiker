import matplotlib.pyplot as plt
import numpy as np

n = 6
s = 1.0

imax = 50

u_vec = np.zeros(imax + 1)
u_vec[0] = 6.0
for i in range(1, imax + 1):
    n = 2 * n
    s = np.sqrt(2 - 2 * np.sqrt(1 - (pow(s, 2)) / 4))
    u_vec[i] = n * s

plt.figure(1)
i_vec = np.arange(imax + 1)
plt.plot(i_vec, u_vec)
plt.grid()
plt.title("A3")

plt.show()
