import matplotlib.pyplot as plt

# Plotting
def plot_func(t, best_pos):
	plt.plot(t, best_pos, marker='o', linestyle='-')  # Plotting the data
	plt.xlabel('Iterations')  # Label for x-axis
	plt.ylabel('Best Score')  # Label for y-axis
	plt.title('Best_score v/s Max_Iterations')  # Title of the plot
	plt.grid(True)  # Adding grid
	plt.show()  # Display the plot
