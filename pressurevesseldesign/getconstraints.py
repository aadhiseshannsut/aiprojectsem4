# uses Penalty method to find the optimal solution

def getconstraints(fnonlin,u):
   # R : Penalty constant >> 1
   R = 10 ** 15
   z = 0
   
   # Get nonlinear constraints
   g,geq = fnonlin(u)[0], fnonlin(u)[1]
   
   # Apply all inequality constraints 
   for gx in g:
       z += R * (getH(gx) ** 2)
       # same as f(x) = f(x) + R*(<g(x)>**2)
          # <g(x)> = 0, if g(x) <= 0
 
 
   # Apply all equality constraints
   for gx in geq:
      z += R * (geteqH(gx) ** 2)
       # same as f(x) = f(x) + R*(<g(x)>**2)
          # <g(x)> = 0, if g(x) == 0
   
   return z


def getH(g):
    return 0 if (g <= 0) else g
    
def geteqH(g):
   return 0 if (g == 0) else g