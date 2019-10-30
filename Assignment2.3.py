"""Write a program which accept one number from user and return its factorial."""

def factorial(n):
	if (n<=0 or n==1):
		return 1
	else:
		return n*factorial(n-1)

print(factorial(5))