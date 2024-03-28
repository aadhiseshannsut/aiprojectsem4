def constraint(x):
    g = [0, 0, 0, 0]
    geq = [] # since there are no equality constraints
    
    # Inequality constraint 1
    g[0] = -x[0] + 0.0193 * x[2]

    # Inequality constraint 2
    g[1] = -x[1] + 0.00954 * x[2]

    # Inequality constraint 3
    g[2] = -3.14159 * x[2]**2 * x[3] - 3.14159 * x[2]**3 + 1296000

    # Inequality constraint 4
    g[3] = x[3] - 240
    
    return g, geq
    