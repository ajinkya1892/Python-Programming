# 2. Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
# CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable
# Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount
# from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
# which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.

class BankAccount:
	ROI=10.5
	def __init__(self,name,value):
		self.Name = name
		self.Amount = value

	def Deposite(self,amount):
		self.Amount += amount

	def Withdraw(self,amount):
		self.Amount -= amount

	def CalulateInterest(self,n):
		interest  =  (self.Amount * n * BankAccount.ROI ) /100
		print ("The interest %s will get on %d is %d after %d years"%(self.Name,self.Amount,interest,n))

	def Display(self):
		print ("The customer is ",self.Name)
		print ("Amount he holds : ",self.Amount)


def main():
	obj1 = BankAccount("Amir", 5000)
	obj1.Display()
	obj1.CalulateInterest(5)

	obj2 = BankAccount("Samir", 3000)
	obj2.Display()
	obj2.CalulateInterest(7)

	obj3 = BankAccount("Kabir", 7000)
	obj3.Display()
	obj3.CalulateInterest(3)

	print("\n")
	obj1.Deposite(3000)
	obj1.Display()
	obj2.Withdraw(100)
	obj2.Display()
	obj2.CalulateInterest(3)


if __name__ == "__main__":
	main()