"""Write a program which display first 10 even numbers on screen.
Output : 2 4 6 8 10 12 14 16 18 20"""

def print_even(n):
	for num in range(2,n*2+2,2):
		print(num)

print_even(10)