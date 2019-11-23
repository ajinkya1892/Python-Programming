# 4.Design python application which creates three threads as small, capital, digits. All the
# threads accepts string as parameter. Small thread display number of small characters,
# capital thread display number of capital characters and digits thread display number of
# digits. Display id and name of each thread.
import threading
import os
def small(st):
	print("This function displays small characters")
	print ("process id of small function:",os.getpid())
	small_list = []
	small_list = [char for char in st if char.isupper()]
	print small_list
	print " number of small case letters"
	print len(small_list)

def Capital(st):
	print("This function displays Capital characters")
	print ("process id of Capital function:",os.getpid())
	capital_list = [char for char in st if char.islower()]
	print capital_list
	print " number of upper case letters"
	print len(capital_list)

def digits(st):
	print("This function displays digits")
	print ("process id of digits function:",os.getpid())
	digit_list = [char for char in st if char.isdigit()]
	print " number of digits"
	print len(digit_list)

def main():
	str = "Ajinkya123"
	t1 = threading.Thread(small(str))
	t2 = threading.Thread(Capital(str))
	t3 = threading.Thread(digits(str))

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()
if __name__ == "__main__":
	main()


