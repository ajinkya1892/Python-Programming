# 2.Design python application which creates two threads as evenfactor and oddfactor.
# Both the thread accept one parameter as integer. Evenfactor thread will display
# addition of even factors of given number and oddfactor will display addition of odd
# factors of given number. After execution of both the thread gets completed main
# thread should display message as exit from main.
import threading
def evenfactor(number):
	for i in range(1,number+1):
		if number%i==0:
			if(i%2==0):
				print("even factor:",i)

def oddfactor(number):
	for i in range(1,number+1):
		if number%i==0:
			if(i%2!=0):
				print("odd factor:",i)

def main():
	number =  320
	t1= threading.Thread(target=evenfactor, args=(number,))
	t2= threading.Thread(target=oddfactor, args=(number,))

	t1.start()
	t2.start()

	t1.join()
	t1.join()
	print("exit from main")
if __name__ == "__main__":
	main()