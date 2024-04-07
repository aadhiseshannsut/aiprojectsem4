import numpy as np
from scipy.stats import wilcoxon
import POA
import POAM
import fun_info_2017 as f
import plotter as p

score_matrix = np.zeros((30, 2))
p_value_matrix = np.zeros((30,2))

def wilcoxonTest(Fun_name):
    SearchAgents = 50  # Number of Pelicans (population members)
    Max_iterations = 1000  # Maximum number of iterations
    num_runs = 10  # Number of runs for each algorithm

    # Object function information
    fitness, lowerbound, upperbound, dimension = f.fun_info(Fun_name)

    # Arrays to store the best scores from each run
    original_best_scores = np.zeros(num_runs)
    modified_best_scores = np.zeros(num_runs)

    # Running the experiments
    for i in range(num_runs):
        # Running the original algorithm (POA)
        Best_score, Best_pos, POA_curve = POA.POA(SearchAgents, Max_iterations, lowerbound, upperbound, dimension, fitness)
        original_best_scores[i] = Best_score
        
        # Running the modified algorithm (POAM)
        Best_score_mod, Best_pos_mod, POAM_curve = POAM.POA(SearchAgents, Max_iterations, lowerbound, upperbound, dimension, fitness)
        modified_best_scores[i] = Best_score_mod

        # # Optional: plotting results for each run
        # p.plot_func(Max_iterations, POA_curve, f"{Fun_name} Original Run {i+1}")
        # p.plot_func(Max_iterations, POAM_curve, f"{Fun_name} Modified Run {i+1}")

    # Performing the Wilcoxon signed-rank test
    print(f"Original Value {np.mean(original_best_scores)}")
    print(f"Modified Value {np.mean(modified_best_scores)}")


    stat, p_value = wilcoxon(original_best_scores, modified_best_scores,zero_method='zsplit')

    # Output the results
    print("Wilcoxon signed-rank test results:")
    print(f"Function - {Fun_name}")
    print(f"Statistic: {stat}, P-value: {p_value}")

    if p_value < 0.05:
        print("There is a significant difference between the original and modified algorithms.")
    else:
        print("There is no significant difference between the original and modified algorithms.")
    return (original_best_scores, modified_best_scores, p_value)

def main():
    for i in range(1, 21):  # Loop over each function from F1 to F25
        if i in {6,7,8,9,12,13,16}:
            continue
        Fun_name = f'F{i}'  # Name of the test function
        original_best_scores, modified_best_scores, p_value = wilcoxonTest(Fun_name)
        score_matrix[i,0] = np.mean(original_best_scores)
        score_matrix[i,1] = np.mean(modified_best_scores)
        p_value_matrix[i,0] = i
        p_value_matrix[i,1] = format(p_value, ".5f")


    print("Score Matrix")
    print(score_matrix)
    print("P Value Matrix")
    print(p_value_matrix)
    

if __name__ == "__main__":
    main()