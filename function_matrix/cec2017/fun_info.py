# CEC2017
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
    

def f1_sphere(x):
    """
    Sphere Function
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return np.sum(x**2)

def f2_elliptic(x):
    """
    Elliptic Function
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    n = len(x)
    return np.sum([10*6(i/(n-1))*x[i]*2 for i in range(n)])

def f3_bent_cigar(x):
    """
    Bent Cigar Function
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return x[0]*2 + 106*np.sum(x[1:]*2)

def f4_discus(x):
    """
    Discus Function
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    n = len(x)
    return 10*6*x[0]2 + np.sum(x[1:]*2)

def f5_different_powers(x):
    """
    Different Powers Function
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return np.sum(np.abs(x)**(2 + 4*np.arange(len(x))/(len(x)-1)))

def f6_rosenbrock(x):
    """
    Rotated Rosenbrock's Function
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [1, 1, ..., 1]
    """
    return np.sum(100*(x[1:]-x[:-1]*2)2 + (x[:-1]-1)*2)

def f7_schaffer(x):
    """
    Schaffer's F7 Function
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return np.sum(0.5 + (np.sin(np.sqrt(x[i]*2 + x[i+1]2))2 - 0.5) / (1 + 0.001(x[i]*2 + x[i+1]2))*2 for i in range(len(x)-1))

def f8_ackley(x):
    """
    Ackley's Function
    Lower Bound: -32
    Upper Bound: 32
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    a = 20
    b = 0.2
    c = 2*np.pi
    return -a*np.exp(-b*np.sqrt(np.mean(x**2))) - np.exp(np.mean(np.cos(c*x))) + a + np.exp(1)

def f9_weierstrass(x):
    """
    Weierstrass's Function
    Lower Bound: -0.5
    Upper Bound: 0.5
    Dimension: 50
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

def f10_griewank(x):
    """
    Griewank's Function
    Lower Bound: -600
    Upper Bound: 600
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return 1 + np.sum(x**2)/4000 - np.prod(np.cos(x/np.sqrt(np.arange(1,len(x)+1))))

def f11_rastrigin(x):
    """
    Rastrigin's Function
    Lower Bound: -5.12
    Upper Bound: 5.12
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return 10*len(x) + np.sum(x**2 - 10*np.cos(2*np.pi*x))

def f12_schwefel(x):
    """
    Schwefel's Problem 2.21
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return np.max(np.abs(x))

def f13_katsuura(x):
    """
    Katsuura Function
    Lower Bound: -5
    Upper Bound: 5
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    d = len(x)
    f = 1
    for i in range(1, d+1):
        f *= np.prod([1 + i*np.abs(x[j]-np.round(x[j])) for j in range(d)])
    return (10/d*2) * f - 10/d*2

def f14_happy_cat(x):
    """
    HappyCat Function
    Lower Bound: -2
    Upper Bound: 2
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [1, 1, ..., 1]
    """
    alpha = 0.5
    return np.abs(np.sum(x*2) - len(x))alpha + (0.5*np.sum(x*2) + np.sum(x))/len(x) + 0.5

def f15_hgbat(x):
    """
    HGBat Function
    Lower Bound: -2
    Upper Bound: 2
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    alpha = 0.5
    return np.abs(np.sum(x*2)2 - np.sum(x)2)alpha + (0.5*np.sum(x*2) + np.sum(x))/len(x) + 0.5

def f16_katsuura_v2(x):
    """
    Katsuura Function (version 2)
    Lower Bound: -5
    Upper Bound: 5
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    d = len(x)
    f = 1
    for i in range(1, d+1):
        f *= np.prod([1 + i*np.abs(x[j]-np.round(x[j])) for j in range(d)])
    return (10/d*2.5) * f - 10/d*2.5

def f17_schaffersf6(x):
    """
    Schaffersf6 Function
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return np.sum(0.5 + (np.sin(np.sqrt(x[i]*2 + x[i+1]2))2 - 0.5) / (1 + 0.001(x[i]*2 + x[i+1]*2)) for i in range(len(x)-1))

def f18_schaffersf7(x):
    """
    Schaffersf7 Function
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    return np.sum(0.5 + (np.cos(np.sin(np.abs(x[i]*2 - x[i+1]2)))2 - 0.5) / (1 + 0.001(x[i]*2 + x[i+1]2))*2 for i in range(len(x)-1))

def f19_expanded_griewank(x):
    """
    Expanded Griewank's plus Rosenbrock's Function
    Lower Bound: -5
    Upper Bound: 5
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [1, 1, ..., 1]
    """
    f = 0
    for i in range(len(x)-1):
        f += 100*(x[i+1] - x[i]*2)2 + (x[i] - 1)*2
    f += 1 + np.sum(x**2)/4000 - np.prod(np.cos(x/np.sqrt(np.arange(1,len(x)+1))))
    return f

def f20_expanded_scaffer(x):
    """
    Expanded Scaffer's F6 Function
    Lower Bound: -100
    Upper Bound: 100
    Dimension: 50
    Optimal Value: f(x*) = 0, x* = [0, 0, ..., 0]
    """
    f = 0
    for i in range(len(x)-1):
        f += 0.5 + (np.sin(np.sqrt(x[i]*2 + x[i+1]2))2 - 0.5) / (1 + 0.001(x[i]*2 + x[i+1]2))*2
    return f