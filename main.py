import tempPOA as t
import fun_info as f
import plotter as p

Fun_name = 'F1'  # number of test functions: 'F1' to 'F23' ** only F1 is used
SearchAgents = 30  # number of Pelicans (population members)
# Max_iterations = 1000  # maximum number of iterations

xaxis = []
yaxis = []

# Object function information
fitness, lowerbound, upperbound, dimension = f.fun_info(Fun_name)

# Calculating the solution of the given problem using POA
for Max_iterations in range(1, 4, 1):
	
	Best_score, Best_pos, POA_curve = t.POA(SearchAgents, Max_iterations, lowerbound, upperbound, dimension, fitness)

	# Displaying results
	print(f"The best solution obtained by POA for {Fun_name} is: \n{Best_pos}")
	print(f"The best optimal value of the objective function found by POA for {Fun_name} is: {Best_score}")
	
	xaxis.append(Max_iterations)
	yaxis.append(Best_score*0.0001)

	print()


p.plot_func(xaxis, yaxis)
print(xaxis)
print(yaxis)