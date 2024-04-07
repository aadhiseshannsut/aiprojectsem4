import POA
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
lowerbound = [2.6, 0.7, 17, 7.3, 7.8, 2.9, 5]
upperbound = [3.6, 0.8, 28, 8.3, 8.3, 3.9, 5.5]
dimension = 7
fitness = fun.Fun
fhandle = weight.weight
fnonlin = constraints.constraint

for i in range(1, ROWS+1):
	# Calculating the solution of the given problem using POA	
	Best_score, Best_pos, POA_curve = POA.POA(SearchAgents,
	 Max_iterations, lowerbound, upperbound, dimension, 
	 fitness, fhandle, fnonlin)

	# Displaying results
	print(f"{i})Best solution : {Best_pos}")
	print(f"Best Score : {Best_score}\n")
	plotter.plot_func(Max_iterations, POA_curve, 'Objective Space')
	
	# save scores in a text file
	writer.add_score(Best_pos, Best_score)
# --------------------------------------------------------------------------------------------------------------------------------------------------