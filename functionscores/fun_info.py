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

    # elif F == 'F12':
    #     return F12, -50, 50, 30

    # elif F == 'F13':
    #     return F13, -50, 50, 30

    # elif F == 'F14':
    #     return F14, -65.53, 65.53, 2

    # elif F == 'F15':
    #     return F15, -5, 5, 4

    # elif F == 'F16':
    #     return F16, -5, 5, 2

    # elif F == 'F17':
    #     return F17, [-5, 10], [0, 15], 2

    # elif F == 'F18':
    #     return F18, -5, 5, 2

    # elif F == 'F19':
    #     return F19, 0, 1, 3

    # elif F == 'F20':
    #     return F20, 0, 1, 6

    # elif F == 'F21':
    #     return F21, 0, 10, 4

    # elif F == 'F22':
    #     return F22, 0, 10, 4

    # elif F == 'F23':
    #     return F23, 0, 10, 4

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
def F6(x):
    return np.sum(np.square(np.floor(x+0.5)))

# F7
def F7(x):
    m = x.shape[0]
    x += np.random.rand()
    z = 0
    for i in range(m):
        z += (i+1)*(x[i]**4) 
    return z

# F8
def F8(x):
    return np.sum(-x * np.sin(np.sqrt(np.abs(x))))

# F9
def F9(x):
    m = x.shape[0]
    z = 0
    for i in range(m):
        z += x[i]**2 - 10*np.cos(2*np.pi*x[i]) + 10
    return z
    
# F10
def F10(x):
    m = x.shape[0]
    R = -20 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / m)) - np.exp(np.sum(np.cos(2 * np.pi * x)) / m) + 20 + np.exp(1)
    return R

# F11
def F11(x):
    m = x.shape[0]
    term1 = 0
    term2 = 1
    for i in range(m):
        term1 += x[i]**2
        term2 *= np.cos(x[i]/((i+1)**0.5))
        
    return term1/4000 - term2 + 1



# # u(xi, a, i, n)
# def u(xi, a, i, n):
    
# # F12
# def F12(x):
#     return np.sum(np.abs(x)) + np.prod(np.abs(x))

# # F13
# def F13(x):
#     m = x.shape[0]
#     term1 = 0
#     term2 = 0
#     term3 = 0
#     p = np.sin(3*np.pi*x[0])
#     q = (x[m-1] - 1)**2 * (1 + np.sin(2*pi*x[m-1]))
    
#     for i in range(m):
#         term1 += (x[i] - 1)**2 * (1 + sin(3*np.pi*x[i])) + p + q
#         term2 +=         
        
        
    

# # F14
# def F14(x):
    
#     m = x.shape[0]
#     term1 = 0
#     for j in range(1, 26):
#         term2 = 0
#         for i in range(2):
            
#         term1 += 1/ ()
    
#     z = 1/500 + np.max(abs(x))
    
#     return 1/ z
# review


# # F15
# def F15(x):
#     m = x.shape[0]
#     z = 0
#     for i in range(m-1):
#         z += 100 * (x[i+1] - x[i]**2)**2 + (x[i]-1)**2
        
#     return z

# # F6
# def F6(x):
#     return np.sum(np.square(np.floor(x+0.5)))

# # F7
# def F7(x):
#     m = x.shape[0]
#     x += np.random.rand()
#     z = 0
#     for i in range(m):
#         z += (i+1)*(x[i]**4) 
#     return z

# # F8
# def F8(x):
#     return np.sum(-x * np.sin(np.sqrt(np.abs(x))))

# # F10
# def F10(x):
#     m = x.shape[0]
#     R = -20 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / m)) - np.exp(np.sum(np.cos(2 * np.pi * x)) / m) + 20 + np.exp(1)
#     return R
