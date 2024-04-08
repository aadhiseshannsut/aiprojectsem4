# objective function
def cost(x):
    x1, x2, x3, x4 = x
    cost = (0.6224*x1*x3*x4) + (1.778*x2*(x3**2)) + (3.1661*(x1**2)*x4) + (19.84*(x1**2)*x3)
    return cost