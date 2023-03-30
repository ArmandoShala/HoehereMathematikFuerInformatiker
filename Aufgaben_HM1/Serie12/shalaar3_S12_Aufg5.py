import numpy as np

A = np.array([[1, 1, 0], [3, -1, 2], [2, -1, 3]])
v = np.array([1, 0, 0]).reshape((3, 1))

tol = pow(1, -6)
v2 = v
k = 0
lambada = np.nan

while np.linalg.norm(v2 - v, 2) > tol or k == 0:
    v = v2
    v2 = (A@v) / np.linalg.norm(A@v, 2)
    k = k + 1
    lambada = (v.T @ A @ v) / (v.T @ v)

    print("K=", k)
    print("lambada=", lambada)
    print("v=", v2)

[W, V] = np.linalg.eig(A)
maxEW = np.argmax(W)
print("Maximale EW ist: ", W[maxEW])
print("Mit dem EV: ", V[:maxEW])
