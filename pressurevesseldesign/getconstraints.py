def getconstraints(fnonlin,u):
   # R : Penalty constant >> 1 
   R = 10 ** 15
   lam, lameq = R, R
   z = 0
   
   # Get nonlinear constraints
   g,geq = fnonlin(u)[0], fnonlin(u)[1]
   
   # Apply all inequality constraints as a penalty function 
   for k in range(0, len(g)):
       z += lam * (g[k] ** 2) * getH(g[k])
       # same as f(x) = f(x) + R*(<g(x)>**2)
          # <g(x)> = 0, if g(x) <= 0
 
 
   # Apply all equality constraints (when geq=[], length->0)
   for k in range(0, len(geq)):
      z += lameq * (geq[k] ** 2) * geteqH(geq[k])
       # same as f(x) = f(x) + R*(<g(x)>**2)
          # <g(x)> = 0, if g(x) == 0
          
   return z


def getH(g):
    H = 0 if (g <= 0) else 1    
    return H
    
def geteqH(g):
   H = 0 if (g == 0) else 1
   return H