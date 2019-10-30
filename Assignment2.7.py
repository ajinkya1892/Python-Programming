"""
Write a program which accept one number and display below pattern.
Input : 5
Output :
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""


def pattern_print(n):
	for i in range(1, n + 1):
		print(' '.join(str(e) for e in range(1, n + 1)))

pattern_print(5)