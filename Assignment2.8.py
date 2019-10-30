def pattern_print(n):
	for i in range(1, n + 1):
		print(" ".join([str(j) for j in range(1,i+1)]))

pattern_print(5)