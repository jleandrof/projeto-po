from scipy.optimize import linprog
import numpy as np

c = [-1, -2, -4, -3, -2, -1]
A = [
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1]
    ]

b = [5, 10, 8, 5, 2]

x1_bnds = (0, None)
x2_bnds = (0, None)
x3_bnds = (0, None)
x4_bnds = (0, None)
x5_bnds = (0, None)
x6_bnds = (0, None)

print(linprog(c, A, b, bounds=(x1_bnds, x2_bnds, x3_bnds, x4_bnds, x5_bnds, x6_bnds)))
