import POA
import fun
import fun_info
import constraints
import plotter as p

# --------------------------------------------------------------------------------------------------------------------------------------------------
Fun_name = "F1"  # test function 
SearchAgents = 50  # number of Pelicans (population members)
Max_iterations = 1000  # maximum number of iterations

# Object function information
lowerbound, upperbound, dimension = -100, 100, 30
fitness = fun_info.fun_info(Fun_name)
# fhandle = fun_info.fun_info(Fun_name)
# fnonlin = constraints.constraint(Fun_name)

# Calculating the solution of the given problem using POA
Best_score, Best_pos, POA_curve = POA.POA(SearchAgents, Max_iterations, lowerbound, upperbound, dimension, fitness)

# Displaying results
print(f"The best solution obtained by POA for {Fun_name} is: \n{Best_pos}")
print(f"The best optimal value of the objective function found by POA for {Fun_name} is: {Best_score}")

# plot best score v/s iteration
p.plot_func(Max_iterations, POA_curve, Fun_name)
# --------------------------------------------------------------------------------------------------------------------------------------------------