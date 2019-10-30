"""Write a program which accept one number and display below pattern.
Input : 5
Output : * * * * *
* * * *
* * *
* *
*"""

def print_patter(n):
	for i in range(n,0,-1):
		print((i)*"* ")

print_patter(5)