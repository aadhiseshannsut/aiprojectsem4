import numpy as np

def fun_info(F):
    if F == 'F1':
        return F1, -100, 100, 30  # Sphere Function
    elif F == 'F2':
        return F2, -100, 100, 30  # Schwefel's Problem 2.22
    elif F == 'F3':
        return F3, -100, 100, 30  # Schwefel's Problem 1.2
    elif F == 'F4':
        return F4, -100, 100, 30  # Schwefel's Problem 2.21
    elif F == 'F5':
        return F5, -100, 100, 30  # Rosenbrock's Function
    elif F == 'F6':
        return F6, -100, 100, 30  # Step Function
    elif F == 'F7':
        return F7, -100, 100, 30  # Quartic Function
    elif F == 'F8':
        return F8, -100, 100, 30  # Schwefel's Problem 2.26
    elif F == 'F9':
        return F9, -100, 100, 30  # Rastrigin's Function
    elif F == 'F10':
        return F10, -100, 100, 30  # Ackley's Function
    elif F == 'F11':
        return F11, -100, 100, 30  # Griewank's Function
    elif F == 'F12':
        return F12, -100, 100, 30  # Penalized Function 1
    elif F == 'F13':
        return F13, -100, 100, 30  # Penalized Function 2
    elif F == 'F14':
        return F14, -100, 100, 30  # Shekel's Foxholes Function
    elif F == 'F15':
        return F15, -100, 100, 30  # Expanded Griewank's plus Rosenbrock's Function
    elif F == 'F16':
        return F16, -100, 100, 2  # Shubert Function
    elif F == 'F17':
        return F17, -100, 100, 2  # Shubert Function
    elif F == 'F18':
        return F18, -100, 100, 2  # Six-Hump Camel-Back Function
    elif F == 'F19':
        return F19, -100, 100, 2  # Easom Function
    elif F == 'F20':
        return F20, -100, 100, 2  # Penalty Function 1
    elif F == 'F21':
        return F21, -100, 100, 2  # Penalty Function 2
    elif F == 'F22':
        return F22, -100, 100, 2  # Penalty Function 3
    elif F == 'F23':
        return F23, -100, 100, 2  # Penalty Function 4
    elif F == 'F24':
        return F24, -100, 100, 2  # Zakharov Function
    elif F == 'F25':
        return F25, -100, 100, 2  # Matyas Function
    elif F == 'F26':
        return F26, -100, 100, 2 
    elif F == 'F27':
        return F27, -100, 100, 2
    elif F == 'F28':
        return F28, -100, 100, 2
    elif F == 'F29':
        return F29, -100, 100, 2 
    elif F == 'F30':
        return F30, -100, 100, 2
    

# F1
def F1(x):
    return np.sum(np.square(x))

# F2
def F2(x):
    return np.sum(np.abs(x)) + np.prod(np.abs(x))

# F3
def F3(x):
    return np.sum(np.cumsum(np.abs(x))**2)

# F4
def F4(x):
    return np.max(np.abs(x))

# F5
def F5(x):
    return np.sum(100.0 * (x[1:] - x[:-1]**2)**2 + (x[:-1] - 1)**2)

# F6: Step Function
def F6(x):
    return np.sum((x + 0.5)**2)

# F7: Quartic Function with Noise
def F7(x):
    return np.sum(np.arange(1, len(x)+1) * (x**4)) + np.random.uniform(0, 1)

# F8: Shifted and Rotated Griewank's Function
def F8(x):
    return 1 + np.sum(x**2 / 4000) - np.prod(np.cos(x / np.sqrt(np.arange(1, len(x) + 1))))

# F9: Shifted Rastrigin's Function
def F9(x):
    return np.sum(x**2 - 10 * np.cos(2 * np.pi * x) + 10)

# F10: Shifted Rotated High Conditioned Elliptic Function
def F10(x):
    n = len(x)
    condition = 1e6
    powers = np.power(condition, np.arange(n) / (n - 1))
    return np.sum(powers * x**2)

# F11: Shifted Rotated Bent Cigar Function
def F11(x):
    return x[0]**2 + 1e6 * np.sum(x[1:]**2)

# F12: Shifted Rotated Discus Function
def F12(x):
    return 1e6 * x[0]**2 + np.sum(x[1:]**2)

# F13: Shifted Sphere Function
def F13(x):
    return np.sum(x**2)

# F14: Shifted Rotated Expanded Griewank plus Rosenbrock Function
def F14(x):
    return (F8(x[:-1] * np.sqrt(F5(x[1:]))))

# F15: Rotated Rosenbrock's Function
def F15(x):
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (x[:-1] - 1)**2)

# F16: Shifted and Rotated Katsuura Function
def F16(x):
    n = len(x)
    product = 1
    for i in range(n):
        product *= (1 + (i + 1) * np.sum(np.abs(2**j * x[i] - round(2**j * x[i])) / 2**j for j in range(1, 33)))
    return (10 / n**2) * product - (10 / n**2)

# F17: Shifted and Rotated HappyCat Function
def F17(x):
    alpha = 1/8
    n = len(x)
    return np.power(np.sum(x**2) - n, 2*alpha) + (0.5*np.sum(x**2)+np.sum(x))/n + 0.5

# F18: Shifted and Rotated HGBat Function
def F18(x):
    n = len(x)
    return np.sqrt(np.abs(np.sum(x**2)**2 - np.sum(x)**2)) + (0.5 * np.sum(x**2) + np.sum(x)) / n + 0.5

# F19: Shifted and Rotated Schwefel's Function
def F19(x):
    n = len(x)
    return 418.9829 * n - np.sum(x * np.sin(np.sqrt(np.abs(x))))

# F20
def F20(x):
    return -(np.sin(np.sqrt(x[0]**2 + x[1]**2)) * np.cos(2 * np.pi * np.sqrt(x[0]**2 + x[1]**2)) / (1 + 0.001 * (x[0]**2 + x[1]**2)))

# F21
def F21(x):
    return -(np.sin(2 * np.pi * np.sqrt(x[0]**2 + x[1]**2)) * (1 + 0.001 * (x[0]**2 + x[1]**2)) / (1 + 0.001 * (x[0]**2 + x[1]**2)))

# F22
def F22(x):
    return -(np.sin(2 * np.pi * np.sqrt(x[0]**2 + x[1]**2)) * (1 + 0.001 * (x[0]**2 + x[1]**2)) / (1 + 0.001 * (x[0]**2 + x[1]**2))) - x[0]

# F23
def F23(x):
    return -(np.sin(2 * np.pi * np.sqrt(x[0]**2 + x[1]**2)) * (1 + 0.001 * (x[0]**2 + x[1]**2)) / (1 + 0.001 * (x[0]**2 + x[1]**2))) - x[1]

# F24
def F24(x):
    return -20 * np.exp(-0.2 * np.sqrt(x[0]**2 + x[1]**2)) - np.exp((np.cos(2 * np.pi * x[0]) + np.cos(2 * np.pi * x[1])) / 2) + 20 + np.e

def F25(x):
    # Hypothetical hybrid function combining features of several basic functions
    return np.sum(np.square(x - 2)) + np.sum(np.abs(x)) + np.prod(np.abs(x))

def F26(x):
    # Hypothetical dynamic environment simulation
    t = np.arange(1, len(x)+1)
    return np.sum(t * x**2)

def F27(x):
    # Composite function including a rotated version of a basic function
    rotation_matrix = np.random.rand(len(x), len(x))  # Random rotation, for example purposes
    x_rotated = np.dot(rotation_matrix, x)
    return np.sum(np.abs(x_rotated - np.mean(x))) + np.prod(np.sin(x_rotated))

def F28(x):
    # Hypothetical function with noise and other challenges
    noise = np.random.normal(0, 1, len(x))
    return np.sum(x**2 + 10*np.cos(2*np.pi*x) + noise)

def F29(x):
    # Function involving conditional elements
    return np.where(x < 0, x**2, -x)

def F30(x):
    # Function that combines multiple characteristics, such as multimodality and high dimensionality
    return np.sum(x**4 - 16*x**2 + 5*x) / 2 + np.sum(100*(x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)
