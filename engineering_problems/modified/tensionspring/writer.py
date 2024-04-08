# append score to a text file in the 'scores' directory and add a new line
def add_score(sol, score):
	bestscores = './scores/best_scores.txt'
	bestsol = './scores/best_sols.txt'
	with open(bestsol, 'a+') as f1:
		with open(bestscores, 'a+') as f2:
			f1.write(str(sol)+'\n')
			f2.write(str(score)+'\n')