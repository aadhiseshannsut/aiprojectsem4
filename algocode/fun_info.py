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
    
    elif F == 'f5_rosenbroc': 
        return f5_rosenbroc, -100, 100, 50
    
    elif F == 'f8_schwefel': 
        return f8_schwefel, -100, 100, 50
    
    elif F == 'f13_schwefel': 
        return f13_schwefel, -100, 100, 30
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

def f5_rosenbroc(x):
    """
    Rosenbrock's Function
    Lower Bound: -30
    Upper Bound: 30
    Dimension: 30
    Optimal Value: f(x*) = 0, x* = [1, 1, ..., 1]
    """
    return np.sum(100*(x[1:]-x[:-1]**2)**2 + (x[:-1]-1)**2)

def f8_schwefel(x):
    """
    Schwefel's Problem 2.6
    Lower Bound: -500
    Upper Bound: 500
    Dimension: 30
    Optimal Value: f(x*) = -418.9829 * D, x* = [420.9687, 420.9687, ..., 420.9687]
    """
    return -np.sum(x * np.sin(np.sqrt(np.abs(x))))

def f13_schwefel(x):
    """
    Hybrid Function 1
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 30
    Optimal Value: f(x*) = 300, x* = [420.9687, 420.9687, ..., 420.9687, 1, 1, ..., 1]
    """
    return 0.8*f8_schwefel(x[:len(x)//2]) + 0.2*f5_rosenbroc(x[len(x)//2:])