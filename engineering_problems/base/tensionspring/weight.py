# objective function
def weight(x):
    x1, x2, x3 = x
    wt = (x3+2)*x2*(x1**2)
    return wt