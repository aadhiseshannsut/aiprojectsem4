import POA
import weight
import constraints
import fun
import plotter


# --------------------------------------------------------------------------------------------------------------------------------------------------
SearchAgents = 30  # number of Pelicans (population members)
Max_iterations = 1000  # maximum number of iterations (1_000)

# Object function information
lowerbound = [2.6, 0.7, 17, 7.3, 7.8, 2.9, 5]
upperbound = [3.6, 0.8, 28, 8.3, 8.3, 3.9, 5.5]
dimension = 7
fitness = fun.Fun
fhandle = weight.weight
fnonlin = constraints.constraint

# Calculating the solution of the given problem using POA	
Best_score, Best_pos, POA_curve = POA.POA(SearchAgents,
 Max_iterations, lowerbound, upperbound, dimension, 
 fitness, fhandle, fnonlin)

# Displaying results
print(f"Best solution: \n{Best_pos}")
print(f"Best optimal value of the objective function : {Best_score}")

iterations = [i+1 for i in range(1, Max_iterations)]
plotter.plot_func(iterations, POA_curve, 'Objective Space')
# --------------------------------------------------------------------------------------------------------------------------------------------------