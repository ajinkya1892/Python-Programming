# 3.Design python application which creates two threads as evenlist and oddlist. Both the
# threads accept list of integers as parameter. Evenlist thread add all even elements
# from input list and display the addition. Oddlist thread add all odd elements from input
# list and display the addition.
import threading
import time
def eventhread(list_num):
	even_list = list()
	for i in list_num:
		if i%2==0:
			even_list.append(i)
	print even_list
	print "addidion of even number:"
	print sum(even_list)
def oddthread(list_num):
	odd_list = list()
	for i in list_num:
		if i%2!=0:
			odd_list.append(i)
	print odd_list
	print "addidion of odd number:"
	print sum(odd_list)
def main():
	number = [1,2,3,4,5,6,7,8,9,10]
	t1 = threading.Thread(target=eventhread,args=(number,))
	t2 = threading.Thread(target=oddthread,args=(number,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

if __name__ == "__main__":
	main()
