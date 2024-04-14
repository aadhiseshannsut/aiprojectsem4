import POAM
import weight
import constraints
import fun
import plotter
import writer

ROWS = 1
# --------------------------------------------------------------------------------------------------------------------------------------------------
SearchAgents = 50  # number of Pelicans (population members)
Max_iterations = 1000  # maximum number of iterations (1_000)

# Object function information
lowerbound = [0.05, 0.25, 2]
upperbound = [2, 1.3, 15]
dimension = 3
fitness = fun.Fun
fhandle = weight.weight
fnonlin = constraints.constraint

for i in range(1, ROWS+1):
	# Calculating the solution of the given problem using POA	
	Best_score, Best_pos, POA_curve = POAM.POA(SearchAgents,
	 Max_iterations, lowerbound, upperbound, dimension, 
	 fitness, fhandle, fnonlin)

	# Displaying results
	print(f"{i})Best solution : {Best_pos}")
	print(f"Best Score : {Best_score}\n")
	plotter.plot_func(Max_iterations, POA_curve, 'Objective Space')
	
	# save scores in a text file
	writer.add_score(Best_pos, Best_score)
# --------------------------------------------------------------------------------------------------------------------------------------------------
