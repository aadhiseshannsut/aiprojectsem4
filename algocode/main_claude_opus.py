import numpy as np

class PelicanOptimization:
    def __init__(self, objective_func, dim, pop_size, max_iter, lb, ub):
        self.objective_func = objective_func
        self.dim = dim
        self.pop_size = pop_size
        self.max_iter = max_iter
        self.lb = lb
        self.ub = ub
        self.population = None
        self.fitness = None
        self.best_solution = None
        self.best_fitness = float('inf')

    def initialize_population(self):
        self.population = np.random.uniform(self.lb, self.ub, (self.pop_size, self.dim))

    def evaluate_population(self):
        self.fitness = np.apply_along_axis(self.objective_func, 1, self.population)

    def update_best_solution(self):
        best_index = np.argmin(self.fitness)
        if self.fitness[best_index] < self.best_fitness:
            self.best_solution = self.population[best_index]
            self.best_fitness = self.fitness[best_index]

    def update_population(self, t):
        for i in range(self.pop_size):
            r1 = np.random.uniform(0, 1)
            r2 = np.random.uniform(0, 1)
            r3 = np.random.uniform(0, 1)

            if r1 < 0.5:
                # Exploration phase
                self.population[i] = self.population[i] + r2 * (self.best_solution - self.population[i]) + r3 * (self.population[np.random.randint(self.pop_size)] - self.population[i])
            else:
                # Exploitation phase
                self.population[i] = self.best_solution + r2 * (self.best_solution - self.population[i])

            # Boundary check
            self.population[i] = np.clip(self.population[i], self.lb, self.ub)

    def run(self):
        self.initialize_population()
        self.evaluate_population()
        self.update_best_solution()

        for t in range(self.max_iter):
            self.update_population(t)
            self.evaluate_population()
            self.update_best_solution()

        return self.best_solution, self.best_fitness

# Example usage
def sphere(x):
    return np.sum(x**2)

dim = 10
pop_size = 50
max_iter = 100
lb = -5.12
ub = 5.12

poa = PelicanOptimization(sphere, dim, pop_size, max_iter, lb, ub)
best_solution, best_fitness = poa.run()

print("Best solution:", best_solution)
print("Best fitness:", best_fitness)