"""Write a program which accept number from user and return addition of digits in that number.
Input : 5187934 Output : 37"""

def add_of_digits(n):
	sum=0
	while(n>0):
		sum+=n%10
		n=n/10
	return sum

print add_of_digits(5187934)