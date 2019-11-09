def ChkPrime(num1):
	# print num1
	if num1 > 1:
			# Iterate from 2 to n / 2
		for i in range(2, num1 ):
				# If num is divisible by any number between
				# 2 and n / 2, it is not prime
			# print num1
			# print  i
			# print (num1 % i//2)
			if (num1 % i) == 0:
				return False
				break
		else:
			return True
	else:
		return False

# print(ChkPrime(45))