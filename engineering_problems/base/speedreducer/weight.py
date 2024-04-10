# objective function
# weight minimization
def weight(x):
    x1, x2, x3, x4, x5, x6, x7 = x
    
    term1 = 0.7854 * x1 * (x2 ** 2) * (3.3333 * (x3 ** 2) + 14.9334 * x3 - 43.0934)
    term2 = -1.508 * x1 * (x6 ** 2 + x7 ** 2)
    term3 = 7.4777 * (x6 ** 3 + x7 ** 3)
    term4 = 0.7854 * (x4 * x6 ** 2 + x5 * x7 ** 2)
    
    return term1 + term2 + term3 + term4