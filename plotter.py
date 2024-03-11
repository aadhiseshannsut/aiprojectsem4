import matplotlib.pyplot as plt

# Plotting
def plot_func(t, best_pos):
	plt.plot(t, best_pos, marker='o', linestyle='-')  # Plotting the data
	plt.xlabel('Iterations')  # Label for x-axis
	plt.ylabel('Best Score')  # Label for y-axis
	plt.title('Best_score v/s Max_Iterations')  # Title of the plot
	plt.grid(True)  # Adding grid
	plt.show()  # Display the plot

# def plot_funcs(t, solutions):
# 	# Initialise the subplot function using number of rows and columns 
# 	n = len(solutions)+1
# 	for i in range(1, n):
# 		plt.subplot(2,2,i)
# 		plt.plot(t,solutions[i-1])
# 		plt.xlabel('Iterations')  # Label for x-axis
# 		plt.ylabel('Best Score')  # Label for y-axis
# 		plt.title(f"F{i}")  # Title of the plot
# 		plt.grid(True)  # Adding grid
	  
# 		# Combine all the operations and display
# 		plt.show() 