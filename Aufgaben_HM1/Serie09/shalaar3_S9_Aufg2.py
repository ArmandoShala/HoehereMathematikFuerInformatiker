import numpy as np


def a2(A, A_err, b, b_err):
    dx_max = np.nan

    x = np.linalg.solve(A, b)
    x_err = np.linalg.solve(A_err, b_err)

    A_norm = np.linalg.norm(A - A_err, np.inf) / np.linalg.norm(A, np.inf)
    d_norm = np.linalg.norm(b - b_err, np.inf) / np.linalg.norm(b, np.inf)
    A_cond = np.linalg.cond(A, np.inf)

    if (A_cond * A_norm < 1):
        dx_max = A_cond / (1 - A_cond * A_norm) * (A_norm + d_norm)

    dx_obs = np.linalg.norm(x - x_err, np.inf) / np.linalg.norm(x, np.inf)

    return (x, x_err, dx_max, dx_obs)


A = np.array(
    [
        [20, 30, 10],
        [10, 17, 6],
        [2, 3, 2]
    ]
)

b = np.array(
    [
        [5720],
        [3300],
        [836]
    ]
)

A_err = A - 0.01
b_err = b + 100

[x, x_err, dx_max, dx_obs] = a2(A, A_err, b, b_err)

print('x', x)
print('x_err', x_err)
print('dx_max', dx_max)
print('dx_obs', dx_obs)
