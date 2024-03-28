import POA
import cost
import constraints
import fun
import plotter


# --------------------------------------------------------------------------------------------------------------------------------------------------
SearchAgents = 30  # number of Pelicans (population members)
Max_iterations = 50  # maximum number of iterations

# Object function information
lowerbound = [0,0,10,10]
upperbound = [100, 100, 200, 200]
dimension = 4
fitness = fun.Fun
fhandle = cost.cost
fnonlin = constraints.constraint

# Calculating the solution of the given problem using POA	
Best_score, Best_pos, POA_curve = POA.POA(SearchAgents,
 Max_iterations, lowerbound, upperbound, dimension, 
 fitness, fhandle, fnonlin)

# Displaying results
print(f"The best solution obtained by POA for area is: \n{Best_pos}")
print(f"The best optimal value of the objective function found by POA for area is: {Best_score}")

plotter.plot_func(iterations, POA_curve, 'Objective Space')

# --------------------------------------------------------------------------------------------------------------------------------------------------