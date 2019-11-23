# 1.Design python application which creates two thread named as even and odd. Even
# thread will display first 10 even numbers and odd thread will display first 10 odd
# numbers.
import threading
import os

def even(number):
	for i in range(number):
		if (i%2==0):
			print("even no is:",i)

def odd(number):
	for i in range(number):
		if (i%2!=0):
			print("odd no is:",i)

def main():
	number = 10
	t1 = threading.Thread(target=even(number))
	t2 = threading.Thread(target=odd(number))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

if __name__ == "__main__":
	main()