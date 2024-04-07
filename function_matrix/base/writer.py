# append score to a text file in the 'scores' directory and add a new line
def add_score(score, filename):
	filepath = './scores/'+filename+'.txt'
	with open(filepath, 'a+') as f:
		f.write(str(score)+'\n')