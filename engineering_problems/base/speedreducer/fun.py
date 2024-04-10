# fitness function
import getconstraints as g
import constraints
import weight

def Fun(fhandle,fnonlin,u):
    z = fhandle(u)
    # Apply nonlinear constraints by the penalty method
    z = z + g.getconstraints(fnonlin,u)

    return z
    
    
# def main():
#     lst = [3.50021711, 0.7, 17.0, 7.3, 7.8, 3.3502296, 5.28668327]
#     z = Fun(weight.weight, constraints.constraint, lst)
#     print(z)
    
# if __name__ == '__main__':
#     main()