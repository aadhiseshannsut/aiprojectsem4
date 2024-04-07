import numpy as np

def constraint(x):
    
    # Inequality constraint 1
    g1 = -x[0] + 0.0193 * x[2]

    # Inequality constraint 2
    g2 = -x[1] + 0.00954 * x[2]

    # Inequality constraint 3
    g3 = -np.pi * (x[2]**2) * x[3] - 4 * np.pi * (x[2]**3)/3 + 1296000

    # Inequality constraint 4
    g4 = x[3] - 240
    
    return np.array([g1, g2, g3, g4])
    