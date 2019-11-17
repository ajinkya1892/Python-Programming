# 3. Write a program which contains one class named as Arithmetic.
# Arithmetic class contains three instance variables as Value1 ,Value2.
# Inside init method initialise all instance variables to 0.
# There are three instance methods inside class as Accept(), Addition(), Subtraction(),
# Multiplication(), Division().
# Accept method will accept value of Value1 and Value2 from user.
# Addition() method will perform addition of Value1 ,Value2 and return result.
# Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
# Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
# Division() method will perform division of Value1 ,Value2 and return result.
# After designing the above class call all instance methods by creating multiple objects

class Arithmetic:
	def __init__(self):
		self.value1 = 0
		self.value2 = 0
	def Accept(self):
		self.value1 = int(input("Enter the first no :  "))
		self.value2 = int(input("Enter the second no :  "))

	def Addition(self):
		return self.value1 + self.value2
	def Subtraction(self):
		if (self.value2>self.value1):
			return self.value2 - self.value1
		else:
			return self.value1 - self.value2
	def Multiplication(self):
		return self.value2 * self.value1
	def Division(self):
		if (self.value2>self.value1):
			return self.value2 / self.value1
		else:
			return self.value1 / self.value2

def main():
	obj1 = Arithmetic()
	obj1.Accept()
	print "The addition is: ",obj1.Addition()
	print "The Substraction is ",obj1.Subtraction()
	print "The Division is ",obj1.Division()
	print "The Multiplication is ",obj1.Multiplication()
if __name__ == '__main__':
	main()