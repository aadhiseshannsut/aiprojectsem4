"""
X : Population Matrix
	X -> dimensions = No. of Pelicans x m
	type(X[i]) = numpy.float64
	
	rows -> pelican (candidate solution)
	columns -> proposed values

fit : Objective Function Vector
	fit -> dimensions = No. of Pelicans x 1 
	type(fit[i]) = numpy.float64

best_so_far : stores best fitness values for each iteration

X_FOOD : Random row from X
F_FOOD : Fitness value of X_FOOD
	-> equivalent to Fp
	
X_new : (possible) New Candidate solution
	-> calculated using Eq(4)
	-> dimensions = 1 x m
	


# misc
    location, best = min(enumerate(fit), key=lambda x: x[1])
    
    returns the least value from fit


Algorithm
# -------------------------------------------------------------------------
Start POA.

Input the optimization problem information.
Determine the POA population size (N) and the number of iterations (T).

Initialization of the position of pelicans and calculate the objective function.

For t = 1:T

	Generate the position of the prey at random.
	For I = 1:N

		Phase 1: Moving towards prey (exploration phase).
			For j = 1:m
			Calculate new status of the jth dimension using Equation (4).
		End.

		Update the ith population member using Equation (5).
		Phase 2: Winging on the water surface (exploitation phase).
		For j = 1:m.
			Calculate new status of the jth dimension using Equation (6).
		End.

		Update the ith population member using Equation (7).
	End.

	Update best candidate solution.
End.

Output best candidate solution obtained by POA.

End POA.
# -------------------------------------------------------------------------

"""