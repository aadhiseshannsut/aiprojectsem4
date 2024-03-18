import tempPOA as t
import fun_info as f
import plotter as p


# --------------------------------------------------------------------------------------------------------------------------------------------------
# Fun_names = ['F1', 'F2', 'F3', 'F4']  # number of test functions: 'F1' to 'F4' 
Fun_names = ["F8"]  # number of test functions: 'F1' to 'F4' 
SearchAgents = 30  # number of Pelicans (population members)
Max_iterations = 1000  # maximum number of iterations

solutions = []

for Fun_name in Fun_names:
	# Object function information
	fitness, lowerbound, upperbound, dimension = f.fun_info(Fun_name)

	# Calculating the solution of the given problem using POA
		
	Best_score, Best_pos, POA_curve, iterations, best_per_iteration = t.POA(SearchAgents, Max_iterations, lowerbound, upperbound, dimension, fitness)

	# Displaying results
	print(f"The best solution obtained by POA for {Fun_name} is: \n{Best_pos}")
	print(f"The best optimal value of the objective function found by POA for {Fun_name} is: {Best_score}")
	
	# solutions.append(best_per_iteration)

for F in Fun_names:
	p.plot_func(iterations, best_per_iteration, F)

# --------------------------------------------------------------------------------------------------------------------------------------------------



# print(iterations)				#DEBUG
# print(best_per_iteration)		DEBUG
# p.plot_func(iterations, best_per_iteration)
# for solution in solutions: