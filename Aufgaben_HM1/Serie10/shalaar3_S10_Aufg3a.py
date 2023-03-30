import numpy as np


def shalaar3_S10_Aufg3a(A, b, x0, tol, opt):
    if opt == "J":
        D = np.diag(np.diag(A))
        D_inv = np.linalg.inv(D)
        LpR = A - D

        B = -D_inv @ LpR
        c = D_inv @ B
    if opt == 'GS':
        DpL = np.tril(A)
        DpL_inv = np.linalg.inv(DpL)
        R = A - DpL
        B = -DpL_inv @ R
        c = DpL_inv @ b

    B_inf = np.linalg.norm(B, np.inf)

    if B_inf < 1:
        xn = B @ x0 + c
        n = 1
        n2 = np.log(tol * (1 - B_inf) / np.linalg.norm(xn - x0, np.inf)) / np.log(B_inf)
        while (B_inf / (1 - B_inf)) * np.linalg.norm(np.linalg.norm(xn - x0, np.inf)) >= tol:
            x0 = xn
            xn = B @ x0 + c
            n = n + 1
        return (xn, n, n2)
    else:
        return


A = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])
b = np.array([[19], [5], [34]])
x0 = np.array([[1], [-1], [3]])

print(shalaar3_S10_Aufg3a(A, b, x0, 1e-4, "J"))
print(shalaar3_S10_Aufg3a(A, b, x0, 1e-4, "GS"))
