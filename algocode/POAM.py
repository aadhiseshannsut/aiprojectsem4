import numpy as np

def POA(SearchAgents, Max_iterations, lowerbound, upperbound, dimension, fitness):
    best_so_far = []  # Initialize list to store best fitness values over iterations
    fbest = 0

    lowerbound = np.ones(dimension) * lowerbound  # Lower limit for variables
    upperbound = np.ones(dimension) * upperbound  # Upper limit for variables

    # Initialization
    X = np.zeros((SearchAgents, dimension))  # Initialize X as a matrix of zeros

    # Random position initialization
    for i in range(dimension):
        X[:, i] = lowerbound[i] + np.random.rand(SearchAgents) * (upperbound[i] - lowerbound[i])

    fit = np.zeros(SearchAgents)  # Initialize fitness array
    for i in range(SearchAgents):
        L = X[i, :]
        fit[i] = fitness(L)

    for t in range(1, Max_iterations+1):
        best = np.min(fit)
        location = np.argmin(fit)

        if (t == 1) or (best < fbest):
            Xbest = X[location, :]  # Accessing row 'location' from matrix X
            fbest = best

        # Update food location randomly chosen
        k = np.random.permutation(SearchAgents)[0]
        X_FOOD = X[k, :]  # Update X_FOOD with the selected row from X
        F_FOOD = fit[k]   # Update F_FOOD with the fitness value corresponding to the selected row

        for i in range(SearchAgents):
            # PHASE 1: Moving towards prey (exploration phase)
            I = 1 + np.random.randint(2)
            if fit[i] > F_FOOD:
                X_new = X[i, :] + np.random.normal(0, 1, size=(1,)) * (X_FOOD - (I * X[i, :]))  # Modified to normal distribution
            else:
                X_new = X[i, :] + np.random.normal(0, 1, size=(1,)) * (X[i, :] - 1 * X_FOOD)   # Modified to normal distribution

            # Ensure X_new is within the bounds
            X_new = np.maximum(X_new, lowerbound)
            X_new = np.minimum(X_new, upperbound)

            # Updating X_i using equation (5) # Check if the position is worse or better
            f_new = fitness(X_new)
            if f_new <= fit[i]:
                X[i, :] = X_new
                fit[i] = f_new

            # PHASE 2: Winging on the water surface (exploitation phase)
            r = np.random.normal(0, 1, size=(1,))  # Modified to normal distribution
            X_new = X[i, :] + (0.2 * (1 - t / Max_iterations) * (2 * r - 1) * X[i, :])

            # Ensure X_new is within the bounds
            X_new = np.maximum(X_new, lowerbound)
            X_new = np.minimum(X_new, upperbound)

            # Updating X_i using equation (7) // updates if it's better.
            f_new = fitness(X_new)
            if f_new <= fit[i]:
                X[i, :] = X_new
                fit[i] = f_new

        best_so_far.append(fbest)

    return fbest, Xbest, best_so_far
