"""5.Write a program which accept one number for user and check whether number is prime or not."""

def prim(n):
	if(n>1):
		# print(n)
		for i in range(2,n):
			# print(n%i)
			if( (n%i) == 0):
				# print((n%i))
				print("Not a prime number")
				break
		else:
			print("prime number")
	else:
		print("not a prime number")

prim(5)