from scipy.optimize import linprog
import numpy as np

def simplex(c, b):
    """ Minimise costs of transportation using simplex method

       Args:
          c (array-like): List of coeficients of the objective function.
          b (array-like): Constraints.
    """
    for i, item in enumerate(c):
        c[i] = -1 * float(item)

    print(c)
    for i, item in enumerate(b):
        b[i] = 1 * float(item)

    # Simplex Tableu
    A = [
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1]
    ]

    # Constraints example: [7, 5, 7, 1, 6]

    # Bounds | Xi >= 0
    x1_bnds = (0, None)
    x2_bnds = (0, None)
    x3_bnds = (0, None)
    x4_bnds = (0, None)
    x5_bnds = (0, None)
    x6_bnds = (0, None)

    result = linprog(c, A, b, bounds=(x1_bnds, x2_bnds, x3_bnds, x4_bnds, x5_bnds, x6_bnds))
    return result

if __name__ == "__main__":

    b = [7, 5, 7, 1, 6]
    c = [0, 2, 4, 3, 2, 1]

    print(simplex(c, b))
