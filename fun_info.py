import numpy as np

def fun_info(F):
    if F == 'F1':
        return F1, -100, 100, 30

    if F == 'F2':
        return F2, -10, 10, 30

# F1
def F1(x):
    return np.sum(np.square(x))

# F2
def F2(x):
    return np.sum(np.abs(x)) + np.prod(np.abs(x))
