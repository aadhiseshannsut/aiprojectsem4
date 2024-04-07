# fitness function
import getconstraints as g
 
def Fun(fhandle,fnonlin,u):
    z = fhandle(u)
    
    # Apply nonlinear constraints by the penalty method
    z = z + g.getconstraints(fnonlin,u)
    
    return z