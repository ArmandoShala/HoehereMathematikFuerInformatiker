import shalaar3_S6_Aufg2 as a2
import numpy as np


def method_script():
    np.linalg.solve()


A1 = np.array(
    [
          [4, -1, -5]
        , [-12, 4, 17]
        , [32, -10, -41]
    ])
x1 = np.array(
    [
          [-5]
        , [19]
        , [-39]
    ])

A2 = np.array(
    [
          [2, 7, 3]
        , [-4, -10, 0]
        , [12, 34, 9]
    ])
x2 = np.array(
    [
          [25]
        , [-24]
        , [107]
    ])

A3 = np.array(
    [
          [-2, 5, 4]
        , [-14, 38, 22]
        , [6, -9, -27]
    ])
x3 = np.array(
    [
          [25]
        , [-24]
        , [107]
    ])

A4 = np.array(
    [
          [-1, 2, 3, 2, 5, 4, 3, -1]
        , [3, 4, 2, 1, 0, 2, 3, 8]
        , [2, 7, 5, -1, 2, 1, 3, 5]
        , [3, 1, 2, 6, -3, 7, 2, -2]
        , [5, 2, 0, 8, 7, 6, 1, 3]
        , [-1, 3, 2, 3, 5, 3, 1, 4]
        , [8, 7, 3, 6, 4, 9, 7, 9]
        , [-3, 14, -2, 1, 0, -2, 10, 5]
    ])
x4 = np.array(
    [
          [-11]
        , [103]
        , [53]
        , [-20]
        , [95]
        , [78]
        , [131]
        , [-26]
    ])


def printRes(id, matrix, x):
    print("A" + id + " Matrix = \n", matrix)
    print("x" + id + " = \n", x)
    print("x" + id + " by python = \n", np.linalg.solve(matrix, x))
    print("Has difference?", (x != np.linalg.solve(matrix, x)))


A1_res, x1_res = a2.S6_A3(A1, x1)
printRes("1", A1_res, x1_res)

A2_res, x2_res = a2.S6_A3(A2, x2)
printRes("2", A2_res, x2_res)

A3_res, x3_res = a2.S6_A3(A3, x3)
printRes("3", A3_res, x3_res)

A4_res, x4_res = a2.S6_A3(A4, x4)
printRes("4", A4_res, x4_res)

# Es gibt signifikante Unterschiede!
