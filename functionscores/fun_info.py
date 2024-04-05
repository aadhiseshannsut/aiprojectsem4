import numpy as np

def fun_info(F):
    if F == 'F1':
        return F1, -100, 100, 30

    elif F == 'F2':
        return F2, -10, 10, 30

    elif F == 'F3':
        return F3, -100, 100, 30

    elif F == 'F4':
        return F4, -100, 100, 30
    
    elif F == 'F8':
        return F8, -500, 500, 30
        
    elif F == 'F10': 
        return F10, -32, 32, 30
    

# F1
def F1(x):
    return np.sum(np.square(x))

# F2
def F2(x):
    return np.sum(np.abs(x)) + np.prod(np.abs(x))

# F3
def F3(x):
    m = x.shape[0]
    R = np.sum(x[:1])**2
    for i in range(1, m):
        R += np.sum(x[:i+1])**2
    return R

# F4
def F4(x):
    return np.max(abs(x))

# F8
def F8(x):
    return np.sum(-x * np.sin(np.sqrt(np.abs(x))))

# F10
def F10(x):
    m = x.shape[0]
    R = -20 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / m)) - np.exp(np.sum(np.cos(2 * np.pi * x)) / m) + 20 + np.exp(1)
    return R
