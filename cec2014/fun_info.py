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

# high condition elliptic function
def F1(x):
    m = x.shape[0]
    z = 0
    for i in range(m):
        term1 = (10**(6))**(i/(m-1))
        term2 = x[i]**2
        z += term1 * term2
    
    return z

# bent cigar function
def F2(x):
    m = x.shape[0]
    z = x[0]**2
    for i in range(1, m):
        z += 10**6 * x[i]**2
    return z

# discus function
def F3(x):
    m = len(x)
    z = 10**6 * x[0]**2
    for i in range(1, m):
        z += x[i]**2
    return z

# rosenbrock's function
def F4(x):
    m = len(x)
    z = 0
    for i in range(m - 1):
        z += 100 * (x[i]**2 - x[i+1])**2 + (x[i] - 1)**2
    return z
    
# Ackley's function
def F5(x):
    dimension = len(x)
    sum1 = np.sum(x**2)
    sum2 = np.sum(np.cos(2 * np.pi * x))
    term1 = -20 * np.exp(-0.2 * np.sqrt(sum1 / dimension))
    term2 = -np.exp(sum2 / dimension)
    z = term1 + term2 + 20 + np.exp(1)
    return z

# Weierstrass function
# review
def F6(x):
    dimension = len(x)
    k_values = np.arange(kmax + 1)
    a_k = a**k_values
    b_k = b**k_values
    z = np.sum(a_k * np.cos(2 * np.pi * b_k * x))
    z -= dimension * np.sum(a_k * np.cos(np.pi * b_k))
    return z
    
# Griewank's function
def F7(x):
    dimension = len(x)
    sum_sq = np.sum(x**2)
    prod_cos = np.prod(np.cos(x / np.sqrt(np.arange(1, dimension + 1))))
    z = 1 + (sum_sq / 4000) - prod_cos
    return z

# Rastrigin's function
def F8(x):
    m = len(x)
    z = 0
    for i in range(m):
        z += x[i]**2 - 10*np.cos(2*np.pi*x[i]) + 10
        
    return z

# Modified Schwefel’s Function
def F9(x):
    m = len(x)
    sum1 = 0
    
    for i in range(m):
        zi = x[i] +4.209687462275036e+002
        if np.abs(zi) <= 500:
            sum1 += zi*np.sin(np.sqrt(np.abs(zi)))
        elif zi > 500:
            k = 500 - zi%500
            sum1 += k*(np.sin(np.sqrt(np.abs(k)))) - ((zi - 500)**2)/(10000*m)
        elif zi < -500:
            k = np.abs(zi)%500 - 500 
            sum1 += k*(np.sin(np.sqrt(np.abs(k)))) - ((zi + 500)**2)/(10000*m)
                    
    return 418.9829 * m + sum1

# Katsuura Function
def F10(x):
    dimension = len(x)
    result = 1.0
    for i in range(dimension):
        sum_term = 0.0
        for j in range(1, 33):
            term = np.abs(2 ** j * x[i] - np.round(2 ** j * x[i]))
            sum_term += term/(2**j)
            
    result *= np.power(1.0 + (i + 1)*sum_term, 10.0 / (dimension**1.2))
    return (10/(m**2)) * result - (10/(m**2))

# HappyCat Function
def F11(x):
    m = len(x)
    sum_sq = np.sum(x**2)
    term1 = (np.sum(x**2) - m)**(1/4)
    term2 = (0.5*sum_sq + np.sum(x))/m
    return term1 + term2 + 0.5
    
# hgbat function
def F12(x):
    m = len(x)
    sum_sq = np.sum(x**2)
    sum_e = np.sum(x)
    term1 = ((np.sum(x**2))**2 - (sum_e)**2)**(1/2)
    term2 = (0.5*sum_sq + sum_e)/m
    return term1 + term2 + 0.5
    
# Expanded Griewank’s plus Rosenbrock’s Function
def F13(x):
    m = len(x)
    z = 0
    for i in range(m-1):
        z += F7(F4(np.array([x[i], x[i+1]])))
    return z + F7(F4(np.array([x[m-1], x[0]])))

# Expanded Scaffer’s F6 Function
def F14(x):
    m = len(x)
    z = 0
    
    def g(x, y):
        s = x**2 + y**2
        n = 0.5 + np.sin(np.sqrt(s)) - 0.5
        d = (1 + 0.001*(s))**2
        return n/d
    
    for i in range(m-1):
        z += g(x[i], x[i+1])
    
    return z + g(x[m-1], x[0])
    



# shifted functions

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