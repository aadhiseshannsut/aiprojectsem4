import numpy as np

def fun_info(F):
    if F == 'F1':
        return F1, -100, 100, 30  # Sphere Function
    elif F == 'F2':
        return F2, -100, 100, 30  # Schwefel's Problem 1.2
    elif F == 'F3':
        return F3, -100, 100, 30  # Schwefel's Problem 2.21
    elif F == 'F4':
        return F4, -100, 100, 30  # Rosenbrock's Function
    elif F == 'F5':
        return F5, -100, 100, 30  # Ackley's Function
    elif F == 'F6':
        return F6, -100, 100, 30  # Weierstrass Function
    elif F == 'F7':
        return F7, -100, 100, 30  # Griewank's Function
    elif F == 'F8':
        return F8, -100, 100, 30  # Rastrigin's Function
    elif F == 'F9':
        return F9, -100, 100, 30  # Expanded Scaffer's F6 Function
    elif F == 'F10':
        return F10, -100, 100, 30  # Katsuura Function
    elif F == 'F11':
        return F11, -100, 100, 30  # Lunacek Bi-Rastrigin Function
    elif F == 'F12':
        return F12, -100, 100, 30  # Expanded Griewank's plus Rosenbrock's Function
    elif F == 'F13':
        return F13, -100, 100, 30  # Expanded Scaffer's F6 Function
    elif F == 'F14':
        return F14, -100, 100, 30  # Hybrid Function 1
    elif F == 'F15':
        return F15, -100, 100, 30  # Hybrid Function 2
    elif F == 'F16':
        return F16, -100, 100, 30  # Hybrid Function 3
    elif F == 'F17':
        return F17, -100, 100, 30  # Composition Function 1
    elif F == 'F18':
        return F18, -100, 100, 30  # Composition Function 2
    elif F == 'F19':
        return F19, -100, 100, 30  # Composition Function 3
    elif F == 'F20':
        return F20, -100, 100, 30  # Composition Function 4

# F1: Sphere Function
def F1(x):
    return np.sum(np.square(x))

# F2: Bent Cigar Function
def F2(x):
    return x[0]**2 + 1e6 * np.sum(x[1:]**2)

# F3: Discus Function
def F3(x):
    return 1e6 * x[0]**2 + np.sum(x[1:]**2)

# F4: Rosenbrock's Function
def F4(x):
    return np.sum(100.0 * (x[1:] - x[:-1]**2)**2 + (x[:-1] - 1)**2)

# F5: Ackley's Function
def F5(x):
    a = 20
    b = 0.2
    c = 2 * np.pi
    n = len(x)
    sum_sq_term = -b * np.sqrt(np.sum(x**2) / n)
    cos_term = -np.sum(np.cos(c * x)) / n
    return a + np.exp(1) - a * np.exp(sum_sq_term) - np.exp(cos_term)

# F6: Weierstrass Function
def F6(x):
    a = 0.5
    b = 3
    k_max = 20
    sum_res = 0
    for i in range(len(x)):
        for k in range(k_max+1):
            sum_res += (a**k) * np.cos(2 * np.pi * (b**k) * (x[i] + 0.5))
    return sum_res - len(x) * sum((a**k) * np.cos(2 * np.pi * (b**k) * 0.5) for k in range(k_max+1))

# F7: Griewank's Function
def F7(x):
    return 1 + np.sum(x**2 / 4000) - np.prod(np.cos(x / np.sqrt(np.arange(1, len(x)+1))))

# F8: Rastrigin’s Function
def F8(x):
    return 10 * len(x) + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))

# F9: Expanded Griewank plus Rosenbrock Function
def F9(x):
    z = np.concatenate(([1], np.cumprod(x[:-1])))
    return F8(x) + F4(z)

# F10: Shifted Rotated High Conditioned Elliptic Function
def F10(x):
    return np.sum(np.power(10, 6 * np.arange(len(x)) / (len(x)-1)) * np.square(x))

# F11: Shifted Rotated Rastrigin’s Function
def F11(x):
    return 10 * len(x) + np.sum((x - np.pi)**2 - 10 * np.cos(2 * np.pi * (x - np.pi)))

# F12: Shifted Rotated Weierstrass Function
def F12(x):
    a = 0.5
    b = 3
    k_max = 20
    D = len(x)
    return np.sum([np.sum([a**k * np.cos(2 * np.pi * b**k * (xi + 0.5)) for k in range(k_max+1)]) for xi in x]) - D * np.sum([a**k * np.cos(2 * np.pi * b**k * 0.5) for k in range(k_max+1)])

# F13: Shifted Rotated Griewank's Function
def F13(x):
    return 1 + np.sum(x**2 / 4000) - np.prod(np.cos(x / np.sqrt(np.arange(1, len(x)+1))))

# F14: Shifted Rotated Ackley's Function
def F14(x):
    return -20 * np.exp(-0.2 * np.sqrt(np.mean(x**2))) - np.exp(np.mean(np.cos(2 * np.pi * x))) + 20 + np.e

# F15: Shifted Rotated Schwefel’s Function (2.13)
def F15(x):
    return 418.9829 * len(x) - np.sum(x * np.sin(np.sqrt(np.abs(x))))

# F16: Shifted Rotated Katsuura Function
def F16(x):
    n = len(x)
    product = 1
    for i in range(1, n + 1):
        sum_j = np.sum([(abs(2**j * x[i-1] - round(2**j * x[i-1])) / 2**j) for j in range(1, 32)])
        product *= (1 + i * sum_j)**(10 / n**1.2)
    return (10 / n**2) * product - (10 / n**2)

# F17: Shifted Rotated Happy Cat Function
def F17(x):
    alpha = 0.125
    return np.abs(np.sum(x**2) - len(x))**alpha + (0.5 * np.sum(x**2) + np.sum(x)) / len(x) + 0.5

# F18: Shifted Rotated HGBat Function
def F18(x):
    return np.sqrt(np.abs(np.sum(x**2)**2 - np.sum(x)**4)) + (0.5 * np.sum(x**2) + np.sum(x)) / len(x) + 0.5

# F19: Shifted Rotated Expanded Griewank plus Rosenbrock Function
def F19(x):
    z = np.concatenate(([1], np.cumprod(x[:-1])))
    return F13(x[:-1]) + F4(z)

# F20: Shifted Rotated Schaffer's F6 Function
def F20(x):
    return np.sum(0.5 + (np.sin(np.sqrt(x[:-1]**2 + x[1:]**2))**2 - 0.5) / (1 + 0.001 * (x[:-1]**2 + x[1:]**2))**2)