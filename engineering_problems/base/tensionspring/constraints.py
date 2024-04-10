import numpy as np

def constraint(x):
    x1, x2, x3 = x

    g1 = 1 - (x2**3 * x3) / (71785 * x1**4)

    g2 = (4 * x2**2 - x1 * x2) / (12566 * (x2 * x1**3 - x1**4)) + 1 / (5108 * x1**2) - 1

    g3 = 1 - (140.45 * x1) / (x2**2 * x3)

    g4 = (x1 + x2) / 1.5 - 1
    
    return np.array([g1, g2, g3, g4])
