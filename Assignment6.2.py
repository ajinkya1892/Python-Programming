# 2. Write a program which contains one class named as Circle.
# Circle class contains three instance variables as Radius ,Area, Circumference.
# That class contains one class variable as PI which is initialise to 3.14.
# Inside init method initialise all instance variables to 0.0.
# The re a re th ree in s tan ce me thod s in side cla s s a s A c cep t() , Cal cula teA rea() ,
# CalculateCircumference(), Display().
# Accept method will accept value of Radius from user.
# CalculateArea() method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference() method will calculate circumference of circle and store it into instance
# variable Circumference.
# And Display() method will display value of all the instance variables as Radius , Area,
# Circumference.
# After designing the above class call all instance methods by creating multiple objects

class Circle:
	PI = 3.14
	def __init__(self):
		self.radius = 0
		self.Area = 0
		self.Circumference = 0
	def Accept(self):
		self.radius = int(input("Enter the radius"))
	def CalculateArea(self):
		self.Area = 2 * Circle.PI * self.radius * self.radius
	def CalculateCircumference(self):
		self.Circumference = 2 * Circle.PI * self.radius
	def Display(self):
		print("The entered radius of circle is:",self.radius)
		print ("The Area of circle is:",self.Area)
		print ("The Circumference of circle is:",self.Circumference)

def main():
	obj1 = Circle()
	obj1.Accept()
	obj1.Display()

if __name__ == '__main__':
	main()