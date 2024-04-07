import numpy as np


def constraint(x):
    x1, x2, x3, x4, x5, x6, x7 = x

    g1 = 27 / (x1 * x2**2 * x3) - 1

    g2 = 397.5 / (x1 * x2**2 * x3) - 1

    g3 = 1.93 * x4**3 / (x2 * x3 * x6**4) - 1

    g4 = 1.93 * x5**3 / (x2 * x3 * x7**4) - 1

    g5 = np.sqrt(((745 * x4 / (x2 * x3)) ** 2 + 16.9 * (10**6))) / (110 * (x6**3)) - 1
    
    g6 = np.sqrt(((745 * x5 / (x2 * x3)) ** 2 + 157.5 * (10**6))) / (85 * (x7**3)) - 1

    g7 = (x2 * x3 / 40) - 1

    g8 = (5 * x2 / x1) - 1

    g9 = (x1 / (12 * x2)) - 1

    g10 = ((1.5 * x6 + 1.9) / x4) - 1

    g11 = ((1.1 * x7 + 1.9) / x5) - 1

    return np.array([g1, g2, g3, g4, g5, g6, g7, g8, g9])
