"""7. Write a program which contains one function that accept one number from user and returns
true if number is divisible by 5 otherwise return false.
Input : 8 Output : False
Input : 25 Output : True"""

def div_five(n):
	if n%5 == 0:
		return True
	else:
		return False

print(div_five(8))
print(div_five(25))
print(div_five(10))
print(div_five(5))