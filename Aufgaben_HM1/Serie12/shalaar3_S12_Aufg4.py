import numpy as np

delimiter = "============================================================================================================"


def a4(A, k):
    A = np.copy(A)

    P = np.eye(np.shape(A)[0], np.shape(A)[1])

    for i in np.arange(0, k):
        [Q, R] = np.linalg.qr(A)
        A = R @ Q
        P = P @ Q

    return (A, P)


A = np.array([[1, -2, 0], [2, 0, 1], [0, -2, 1]])
[Ak, Pk] = a4(A, 100)

print("A=", Ak, "\nP=", Pk)
print(delimiter)

PkTrans = Pk.T
PkInv = np.linalg.inv(Pk)
if np.linalg.norm(PkTrans - PkInv, np.inf) < pow(1, -10):
    print("P ist orthogonal, da Pk.T = Pk.inverse")
    print(delimiter)

print("Da Ak symmetrisch ist, entsprechen die EW den Diagonalelementen")
for i in np.arange(0, np.shape(Ak)[0]):
    print(Ak[i, i], Pk[:, i])

print(delimiter)

[W, V] = np.linalg.eig(A)
print("EW stehen im Vektor W=", W)
print("EW sind Spalten im Vektor V=", V)
print("j entspricht imaginärer Zahl i")
print(delimiter)
