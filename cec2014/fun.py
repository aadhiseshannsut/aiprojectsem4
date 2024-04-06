# fitness function
import getconstraints as g
 
def Fun(fhandle,fnonlin,u):
    z = fhandle(u)
    # Apply nonlinear constraints by the penalty method
    # Z = f+sum_k = 1^N lam_k g_k^2 *H(g_k) where lam_k >> 1 
    z = z + g.getconstraints(fnonlin,u)
    
    return z