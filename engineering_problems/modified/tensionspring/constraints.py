import numpy as np

def constraint(x):
    x1, x2, x3 = x

    # Constraint 1: Stress under bending must not exceed the material's yield stress
    # Assuming x3 is the number of active coils, x1 is the wire diameter, and x2 is the mean coil diameter
    g1 = 1 - (x2**3 * x3) / (71785 * x1**4)

    # Constraint 2: Surplus of slenderness to avoid buckling
    # Corrected to use only x2 squared, assuming it refers to dimensional properties impacting buckling
    g2 = (4 * x2**2 - x1 * x2) / (12566 * (x2 * x1**3)) + 1 / (5108 * x1**2) - 1

    # Constraint 3: Avoiding shear stress exceeding the limit
    g3 = 1 - (140.45 * x1) / (x2**2 * x3)

    # Constraint 4: Total dimensions relative to a given constant for fitting in an assembly
    g4 = (x1 + x2) / 1.5 - 1
    
    return np.array([g1, g2, g3, g4])
