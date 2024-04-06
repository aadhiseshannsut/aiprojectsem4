import numpy as np

def fun_info(F):
    if F == 'F1':
        return F1

    elif F == 'F2':
        return F2

    elif F == 'F3':
        return F3

    elif F == 'F4':
        return F4
    
    elif F == 'F5':
        return F8
        
    elif F == 'F10': 
        return F10
        
    elif F == 'F10': 
        return F10

    elif F == 'F11': 
        return F10

    elif F == 'F12': 
        return F10

    elif F == 'F13': 
        return F10

    elif F == 'F14': 
        return F10

    elif F == 'F15': 
        return F10

    elif F == 'F16': 
        return F10

    elif F == 'F17': 
        return F10

    elif F == 'F18': 
        return F10

    elif F == 'F19': 
        return F10

    elif F == 'F20': 
        return F10

    elif F == 'F21': 
        return F10

    elif F == 'F22': 
        return F10

    elif F == 'F23': 
        return F10

    elif F == 'F24': 
        return F10

    elif F == 'F25': 
        return F10

    elif F == 'F26': 
        return F10

    elif F == 'F27': 
        return F10

    elif F == 'F28': 
        return F10

    elif F == 'F29': 
        return F10

    elif F == 'F30': 
        return F10

def F1(x):
    """
    Sphere Function
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 30
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return np.sum(x**2)

def f2_schwefel(x):
    """
    Schwefel's Problem 2.22
    Lower Bound: -10
    Upper Bound: 10
    Dimension: 30
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return np.sum(np.abs(x)) + np.prod(np.abs(x))

def f3_schwefel(x):
    """
    Schwefel's Problem 1.2
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 30
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return np.sum([np.sum(x[:i+1])**2 for i in range(len(x))])

def f4_schwefel(x):
    """
    Schwefel's Problem 2.21
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 30
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return np.max(np.abs(x))

def f5_rosenbroc(x):
    """
    Rosenbrock's Function
    Lower Bound: -30
    Upper Bound: 30
    Dimension: 30
    Optimal Value: f(x*) = 0, x* = [1, 1, ..., 1]
    """
    return np.sum(100*(x[1:]-x[:-1]*2)2 + (x[:-1]-1)*2)

def f6_step(x):
    """
    Step Function
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 30
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return np.sum(np.floor(x+0.5)**2)

def f7_quartic(x):
    """
    Quartic Function
    Lower Bound: -1.28
    Upper Bound: 1.28
    Dimension: 30
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return np.sum(np.abs(x)**4)

def f8_schwefel(x):
    """
    Schwefel's Problem 2.6
    Lower Bound: -500
    Upper Bound: 500
    Dimension: 30
    Optimal Value: f(x*) = -418.9829 * D, x* = [420.9687, 420.9687, ..., 420.9687]
    """
    return -np.sum(x * np.sin(np.sqrt(np.abs(x))))

def f9_rastrigin(x):
    """
    Rastrigin's Function
    Lower Bound: -5.12
    Upper Bound: 5.12
    Dimension: 30
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return 10*len(x) + np.sum(x**2 - 10*np.cos(2*np.pi*x))

def F5(x):
    """
    Ackley's Function
    Lower Bound: -32
    Upper Bound: 32
    Dimension: 30
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    m = x.shape[0]
    term1 = -20*np.exp(-0.2*np.sqrt(np.sum(np.square(x))/m))
    term2 = np.exp(np.cos(2*np.pi*x)/m)
    return term1 - term2 + 20 + np.exp(1)

def f11_griewank(x):
    """
    Griewank's Function
    Lower Bound: -600
    Upper Bound: 600
    Dimension: 30
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return 1 + np.sum(x**2)/4000 - np.prod(np.cos(x/np.sqrt(np.arange(1,len(x)+1))))

def f12_weierstrass(x):
    """
    Weierstrass's Function
    Lower Bound: -0.5
    Upper Bound: 0.5
    Dimension: 30
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    a = 0.5
    b = 3
    k_max = 20
    d = len(x)
    f = 0
    for i in range(d):
        f += np.sum([a*k * np.cos(b*k * np.pi * (x[i] + 0.5)) for k in range(k_max)])
    return f - d * np.sum([a*k * np.cos(b*k * np.pi * 0.5) for k in range(k_max)])

def f13_schwefel(x):
    """
    Hybrid Function 1
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 30
    Optimal Value: f(x*) = 300, x* = [420.9687, 420.9687, ..., 420.9687, 1, 1, ..., 1]
    """
    return 0.8*f8_schwefel(x[:len(x)//2]) + 0.2*f5_rosenbroc(x[len(x)//2:])

def f14_schwefel(x):
    """
    Hybrid Function 2
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 30
    Optimal Value: f(x*) = 300, x* = [420.9687, 420.9687, ..., 420.9687, 0, 0, ..., 0]
    """
    return 0.8*f3_schwefel(x[:len(x)//2]) + 0.2*f10_ackley(x[len(x)//2:])

def f15_schwefel(x):
    """
    Hybrid Function 3
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 30
    Optimal Value: f(x*) = 310, x* = [0, 0, ..., 0, 0, 0, ..., 0, 0, 0, ..., 0]
    """
    return 0.5*f6_step(x[:len(x)//3]) + 0.3*f9_rastrigin(x[len(x)//3:2*len(x)//3]) + 0.2*f1_sphere(x[2*len(x)//3:])

def f16_schwefel(x):
    """
    Composition Function 1
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 30
    Optimal Value: f(x*) = 100, x* = [420.9687, 420.9687, ..., 420.9687]
    """
    sigma = [10, 20, 30, 40, 50]
    lambda_ = [1, 1e-6, 1e-26, 1e-6, 1e-6]
    tau = [0.2, 0.2, 0.2, 0.2, 0.2]
    bias = [0, 100, 200, 300, 400]
    
    f = 0
    for i in range(len(sigma)):
        f += lambda_[i] * (f8_schwefel(x/sigma[i]) + bias[i])
    
    return f / np.sum(lambda_)

def f17_schwefel(x):
    """
    Composition Function 2
    Lower Bound: -5
    Upper Bound: 5
    Dimension: 30
    Optimal Value: f(x*) = 200, x* = [0, 0, ..., 0]
    """
    sigma = [10, 10, 10, 10, 10] 
    lambda_ = [1, 1e-6, 1e-26, 1e-6, 1e-6]
    tau = [0.2, 0.2, 0.2, 0.2, 0.2]
    bias = [0, 100, 200, 300, 400]
    
    f = 0
    for i in range(len(sigma)):
        f += lambda_[i] * (f9_rastrigin(x/sigma[i]) + bias[i])
    
    return f / np.sum(lambda_)

def f18_schwefel(x):
    """
    Composition Function 3
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 30
    Optimal Value: f(x*) = 300, x* = [1, 1, ..., 1]
    """
    sigma = [10, 10, 10, 10, 10]
    lambda_ = [1, 1e-6, 1e-26, 1e-6, 1e-6] 
    tau = [0.2, 0.2, 0.2, 0.2, 0.2]
    bias = [0, 100, 200, 300, 400]
    
    f = 0
    for i in range(len(sigma)):
        f += lambda_[i] * (f5_rosenbroc(x/sigma[i]) + bias[i])
    
    return f / np.sum(lambda_)

def f19_schwefel(x):
    """
    Composition Function 4
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 30
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    sigma = [10, 10, 10, 10, 10]
    lambda_ = [1, 1e-6, 1e-26, 1e-6, 1e-6]
    tau = [0.2, 0.2, 0.2, 0.2, 0.2]
    bias = [0, 100, 200, 300, 400]
    
    f = 0
    for i in range(len(sigma)):
        f += lambda_[i] * (f1_sphere(x/sigma[i]) + bias[i])
    
    return f / np.sum(lambda_)

def f20_schwefel(x):
    """
    Composition Function 5
    Lower Bound: -600
    Upper Bound: 600
    Dimension: 30
    Optimal Value: f(x*) = 300, x* = [0, 0, ..., 0]
    """
    sigma = [10, 10, 10, 10, 10]
    lambda_ = [1, 1e-6, 1e-26, 1e-6, 1e-6]
    tau = [0.2, 0.2, 0.2, 0.2, 0.2]
    bias = [0, 100, 200, 300, 400]
    
    f = 0
    for i in range(len(sigma)):
        f += lambda_[i] * (f11_griewank(x/sigma[i]) + bias[i])
    
    return f / np.sum(lambda_)

def f21_schwefel(x):
    """
    Composition Function 6
    Lower Bound: -0.5
    Upper Bound: 0.5
    Dimension: 30
    Optimal Value: f(x*) = 200, x* = [0, 0, ..., 0]
    """
    sigma = [10, 10, 10, 10, 10]
    lambda_ = [1, 1e-6, 1e-26, 1e-6, 1e-6]
    tau = [0.2, 0.2, 0.2, 0.2, 0.2]
    bias = [0, 100, 200, 300, 400]
    
    f = 0
    for i in range(len(sigma)):
        f += lambda_[i] * (f12_weierstrass(x/sigma[i]) + bias[i])
    
    return f / np.sum(lambda_)

def f22_schwefel(x):
    """
    Composition Function 7
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 30
    Optimal Value: f(x*) = 300, x* = [420.9687, 420.9687, ..., 420.9687, 1, 1, ..., 1]
    """
    sigma = [10, 10, 10, 10, 10]
    lambda_ = [1, 1e-6, 1e-26, 1e-6, 1e-6]
    tau = [0.2, 0.2, 0.2, 0.2, 0.2]
    bias = [0, 100, 200, 300, 400]
    
    f = 0
    for i in range(len(sigma)):
        f += lambda_[i] * (f13_schwefel(x/sigma[i]) + bias[i])
    
    return f / np.sum(lambda_)

def f23_schwefel(x):
    """
    Composition Function 8
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 30
    Optimal Value: f(x*) = 300, x* = [420.9687, 420.9687, ..., 420.9687, 0, 0, ..., 0]
    """
    sigma = [10, 10, 10, 10, 10]
    lambda_ = [1, 1e-6, 1e-26, 1e-6, 1e-6]
    tau = [0.2, 0.2, 0.2, 0.2, 0.2]
    bias = [0, 100, 200, 300, 400]
    
    f = 0
    for i in range(len(sigma)):
        f += lambda_[i] * (f14_schwefel(x/sigma[i]) + bias[i])
    
    return f / np.sum(lambda_)

def f24_schwefel(x):
    """
    Composition Function 9
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 30
    Optimal Value: f(x*) = 310, x* = [0, 0, ..., 0, 0, 0, ..., 0, 0, 0, ..., 0]
    """
    sigma = [10, 10, 10, 10, 10]
    lambda_ = [1, 1e-6, 1e-26, 1e-6, 1e-6]
    tau = [0.2, 0.2, 0.2, 0.2, 0.2]
    bias = [0, 100, 200, 300, 400]
    
    f = 0
    for i in range(len(sigma)):
        f += lambda_[i] * (f15_schwefel(x/sigma[i]) + bias[i])
    
    return f / np.sum(lambda_)