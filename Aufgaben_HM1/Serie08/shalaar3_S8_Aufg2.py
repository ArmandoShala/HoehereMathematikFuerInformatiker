# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:26:09 2020

Höhere Mathematik 1, Serie 8, Gerüst für Aufgabe 2

Description: calculates the QR factorization of A so that A = QR
Input Parameters: A: array, n*n matrix
Output Parameters: Q : n*n orthogonal matrix
                   R : n*n upper right triangular matrix
Remarks: none
Example: A = np.array([[1,2,-1],[4,-2,6],[3,1,0]])
        [Q,R]=Serie8_Aufg2(A)

@author: knaa
"""
import timeit

import numpy as np


def Serie8_Aufg2(A):
    import numpy as np

    A = np.copy(A)  # necessary to prevent changes in the original matrix A_in
    A = A.astype('float64')  # change to float

    n = np.shape(A)[0]

    if n != np.shape(A)[1]:
        raise Exception('Matrix is not square')

    Q = np.eye(n)
    R = A

    for j in np.arange(0, n - 1):
        a = np.copy(R[j:, j]).reshape(n - j, 1)
        e = np.eye(n - j)[:, 0].reshape(n - j, 1)
        length_a = np.linalg.norm(a)
        if a[0] >= 0:
            sig = 1
        else:
            sig = -1
        v = a + sig * length_a * e
        u = v * 1 / np.linalg.norm(v)
        H = np.eye(n - j) - 2 * u @ u.T
        Qi = np.eye(n)
        Qi[j:, j:] = H[:, :]
        R = Qi @ R
        Q = Q @ Qi.T

        return (Q, R)


def aufg2():
    A = np.array(
        [
              [1 - 2, 3]
            , [-5, 4, 1]
            , [2, -1, 3]
        ]
    )

    b = np.array(
        [
              [1]
            , [9]
            , [5]
        ]
    )

    [Q,R] = Serie8_Aufg2(A)
    x = np.lingalt.solve(R, Q.T@b)
    print(Q)
    print(R)
    print(Q@R)
    print(x)

def aufg3():
    num = 100
    t1 = timeit.repeat("Serie8_Aufg2(A)", "from __main__ import  Serie8_Aufg2(A)")
    t1 = timeit.repeat("np.lingalq.qr(A)", "from __main__ import  np, A")
