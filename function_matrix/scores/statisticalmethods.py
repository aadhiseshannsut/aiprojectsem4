import numpy as np

def main():
	Fun_names = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11']
	for f in Fun_names:
		base = open('./base/'+f+'.txt', 'r')
		modified = open('./modified/'+f+'.txt', 'r')
		
		scores_base = base.read().split('\n')
		scores_modified = modified.read().split('\n')
		
		scores_base = [float(value) for value in scores_base if value]
		scores_modified = [float(value) for value in scores_modified if value]
		
		mean_base = np.mean(scores_base)		
		mean_modified = np.mean(scores_modified)
				
		std_base = np.std(scores_base)		
		std_modified = np.std(scores_modified)

		median_base = np.median(scores_base)		
		median_modified = np.median(scores_modified)
		
		print("Objective Function: ", f)
		print("Mean(base)   	 : ", mean_base)
		print("STD(base)    	 : ", mean_base)
		print("Median(base) 	 : ", mean_base)
		
		print()
		
		print("Mean(modified)   : ", mean_modified)
		print("STD(modified)    : ", mean_modified)
		print("Median(modified) : ", mean_modified)
		
		print("\n\n")
		
		
		base.close()
		modified.close()

if __name__ == '__main__':
	main()