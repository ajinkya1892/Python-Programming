"""Write a program which accept one number and display below pattern.
Input : 5
Output : * * * * *
* * * * *
* * * * *
* * * * *
* * * * *"""

def pattern_star(n):
	for i in range(0,n):
		print (n*"*  ")

pattern_star(5)