import numpy as np
import matplotlib.pyplot as plt
import shalaar3_S9_Aufg2 as s2

n = 200
dim = 100
matrix = np.zeros((n, 3))
x_axis = np.arange(0, n)

for i in x_axis:
    A = np.random.rand(dim, dim)
    A_err = A + A / 1e5
    b = np.random.rand(dim, 1)
    b_err = b + b / 1e5
    [x, x_err, dx_max, dx_obs] = s2.a2(A, A_err, b, b_err)
    matrix[i, 0] = dx_obs
    matrix[i, 1] = dx_max
    matrix[i, 2] = dx_max / dx_obs

plt.semilogy(x_axis, matrix[:, 0], x_axis, matrix[:, 1], x_axis, matrix[:, 2], x_axis)
