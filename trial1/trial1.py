import numpy as np

# Objective function: Sphere function
def objective_function(x):
    return np.sum(x**2)

# Initialize the population
def initialize_population(pop_size, dim, bounds):
    population = np.random.rand(pop_size, dim) * (bounds[1] - bounds[0]) + bounds[0]
    return population

# Evaluate the fitness of all individuals in the population
def evaluate_population(population):
    return np.array([objective_function(individual) for individual in population])

# Update position of each pelican (solution)
def update_position(population, best_idx, bounds, dim, a=2, b=1):
    new_population = np.zeros_like(population)
    for i, pelican in enumerate(population):
        r1, r2 = np.random.rand(2)  # Random coefficients
        A = 2 * a * r1 - a  # Coefficient A
        C = 2 * r2  # Coefficient C
        
        # Diving (Exploitation) or Flight (Exploration)
        if np.random.rand() < 0.5:  # Diving
            distance_to_best = C * (population[best_idx] - pelican)
            new_position = population[best_idx] - A * distance_to_best
        else:  # Flight
            random_idx = np.random.randint(len(population))
            random_pelican = population[random_idx]
            distance_to_random = C * (random_pelican - pelican)
            new_position = pelican - A * distance_to_random
        
        # Ensure the new position is within bounds
        new_population[i] = np.clip(new_position, bounds[0], bounds[1])
    return new_population

# Pelican Optimization Algorithm
def pelican_optimization_algorithm(pop_size, dim, bounds, max_iter):
    population = initialize_population(pop_size, dim, bounds)
    fitness = evaluate_population(population)
    
    for iteration in range(max_iter):
        best_idx = np.argmin(fitness)  # Index of the best solution
        population = update_position(population, best_idx, bounds, dim)
        fitness = evaluate_population(population)
        
        if iteration % 10 == 0:
            print(f"Iteration {iteration}: Best Fitness = {fitness[best_idx]}")
    
    best_solution = population[best_idx]
    best_fitness = fitness[best_idx]
    return best_solution, best_fitness

# Parameters
pop_size = 30  # Population size
dim = 5  # Dimensionality of the problem
bounds = (-10, 10)  # Bounds of the search space
max_iter = 100  # Maximum number of iterations

# Run the algorithm
best_solution, best_fitness = pelican_optimization_algorithm(pop_size, dim, bounds, max_iter)
print(f"Best Solution: {best_solution}, Best Fitness: {best_fitness}")