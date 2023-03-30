import numpy as np

A_orig = np.array([[4, -1, -5], [-12, 4, 17], [32, -10, -41]])
b_orig = np.array([[-5], [19], [-39]])


def S6_A3(A_in, b_in):
    A = np.copy(A_in).astype("float64")
    b = np.copy(b_in).astype("float64")

    n = np.shape(A)[0]

    for i in np.arange(0, n):
        j = i
        while j < n and A[j, i] == 0:
            j = j + 1
        if j != i:
            swap(A, b, i, j)
        for j in np.arange(i + 1, n):
            c = A[j, i] / A[i, i]
            subtract(A, b, j, i, c)
    x = reserve_insert(A, b)
    return A, x


def swap(A, b, i, j):
    tmp = np.copy(A[i, :])
    A[i, :] = A[j, :]
    A[j, :] = tmp
    tmp = np.copy(b[i])
    b[i] = b[j]
    b[j] = tmp
    return A, b


def subtract(A, b, j, i, c):
    A[j, :] = A[j, :] - c * A[i, :]
    b[j] = b[j] - c * b[i]
    return A, b


def reserve_insert(A, b):
    n = np.shape(A)[0]
    x = np.zeros([n, 1])
    for i in np.arange(n - 1, -1, -1):
        x[i] = (b[i] - A[i, i + 1:n] @ x[i + 1:n]) / A[i, i]
    return x


resMatrix, x = S6_A3(A_orig, b_orig)

# print("Matrix:\n", resMatrix)
# print("x:\n", x)
