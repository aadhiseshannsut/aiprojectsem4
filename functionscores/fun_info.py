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

    elif F == 'F5':
        return F5, -30, 30, 30

    elif F == 'F6':
        return F6, -100, 100, 30

    elif F == 'F7':
        return F7, -1.28, 1.28, 30

    elif F == 'F8':
        return F8, -500, 500, 30

    elif F == 'F9':
        return F9, -5.12, 5.12, 30

    elif F == 'F10':
        return F10, -32, 32, 30

    elif F == 'F11':
        return F11, -600, 600, 30

    elif F == 'F12':
        return F12, -50, 50, 30

    elif F == 'F13':
        return F13, -50, 50, 30

    elif F == 'F14':
        return F14, -65.53, 65.53, 2

    elif F == 'F15':
        return F15, -5, 5, 4

    elif F == 'F16':
        return F16, -5, 5, 2

    elif F == 'F17':
        return F17, [-5, 10], [0, 15], 2

    elif F == 'F18':
        return F18, -5, 5, 2

    elif F == 'F19':
        return F19, 0, 1, 3

    elif F == 'F20':
        return F20, 0, 1, 6

    elif F == 'F21':
        return F21, 0, 10, 4

    elif F == 'F22':
        return F22, 0, 10, 4

    elif F == 'F23':
        return F23, 0, 10, 4

    else:
        raise ValueError("Unknown function: " + F)

   

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

# F5
def F5(x):
    m = x.shape[0]
    z = 0
    for i in range(m-1):
        z += 100 * (x[i+1] - x[i]**2)**2 + (x[i]-1)**2
        
    return z

# F6
def F4(x):
    return np.max(abs(x))

# F7
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
