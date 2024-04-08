import matplotlib.pyplot as plt
# -------------------------------------------------------------------------
def plot_func(t, best_pos, F):
	x = [i for i in range(1, t+1)] # number of iterations
	plt.plot(x, best_pos, marker='o', linestyle='-')  # Plotting the data
	plt.xlabel('Iterations')  # Label for x-axis
	plt.ylabel('Best Score')  # Label for y-axis
	plt.title(F)  # Title of the plot
	plt.grid(True)  # Adding grid
	plt.show()  # Display the plot
# -------------------------------------------------------------------------