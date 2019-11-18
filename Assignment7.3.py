# 3. Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
# Factors().
# ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.


class Arithmetic():
	def __init__(self,number):
		self.number = number

	def ChkPrime(self):
		if self.number > 1:

			# Iterate from 2 to n / 2
			for i in range(2, self.number // 2):

				# If num is divisible by any number between
				# 2 and n / 2, it is not prime
				if (self.number % i) == 0:
					return False
					break
			else:
				return True
		else:
			return True

	def ChkPerfect(self):
		sum = 0
		for x in range(1, self.number):
			if self.number % x == 0:
				sum += x
		return sum == self.number

	def Factors(self):
		factors = list()
		for i in range(1, self.number + 1):
			if self.number % i == 0:
				factors.append(i)
		return factors

	def SumFactors(self):
		sum = 0
		faclist = self.Factors()
		for num in faclist:
			sum += num
		return  sum


obj1 = Arithmetic(5)
print ("If prime or not: ",obj1.ChkPrime())
print ("If perfect or not: ",obj1.ChkPerfect())
print ("Factors: ",obj1.Factors())
print ("If sum of factors : ",obj1.SumFactors())
print("\n")

obj2 = Arithmetic(28)
print ("If prime or not: ",obj2.ChkPrime())
print ("If perfect or not: ",obj2.ChkPerfect())
print ("Factors: ",obj2.Factors())
print ("If sum of factors : ",obj2.SumFactors())
print("\n")


obj3 = Arithmetic(13)
print ("If prime or not: ",obj3.ChkPrime())
print ("If perfect or not: ",obj3.ChkPerfect())
print ("Factors: ",obj3.Factors())
print ("If sum of factors : ",obj3.SumFactors())