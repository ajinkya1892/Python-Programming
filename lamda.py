def add(no1,no2):
	return no1+no2

print("The addition of %s and %s is : %d"%(5,10,add(5,10)))

fp = lambda no1,no2:no1+no2
print("The addition of %s and %s is : %d"%(5,10,fp(5,10)))