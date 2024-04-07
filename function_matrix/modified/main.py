import POAM
import fun_info as f
import writer as w

ROWS = 2
# -------------------------------------------------------------------------------------------------------------------------------------------------
Fun_names = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11']
SearchAgents = 50  # number of Pelicans (population members)
Max_iterations = 2000  # maximum number of iterations

for Fun_name in Fun_names:
	print(f"\n Function : {Fun_name}")
	for i in range(1,ROWS+1):
		# Object function information
		fitness, lowerbound, upperbound, dimension = f.fun_info(Fun_name)
			
		# Calculating the solution of the given problem using POA
		Best_score, Best_pos, POA_curve = POAM.POA(SearchAgents, Max_iterations, lowerbound, upperbound, dimension, fitness)

		# Displaying results
		print(f"{i}) Best score : {Best_score}")
		
		# save scores in a text file
		w.add_score(Best_score, Fun_name)

# --------------------------------------------------------------------------------------------------------------------------------------------------