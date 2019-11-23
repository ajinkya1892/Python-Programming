# 5.Design python application which contains two threads named as thread1 and thread2.
# # # Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
# # # screen. After execution of thread1 gets completed then schedule thread2.
import threading
import os
def thread1(lock):
	lock.acquire()
	print ("in thread 1:",os.getpid())
	for i in range(1,51):
		print i
	lock.release()
def thread2(lock):
	lock.acquire()
	print ("in thread 2:",os.getpid())
	for i in range(50,0,-1):
		print i
	lock.release()

def main():
	lock = threading.Lock()
	t1 = threading.Thread(thread1(lock))
	t2 = threading.Thread(thread2(lock))


	t1.start()
	t2.start()

	t1.join()
	t2.join()

if __name__=="__main__":
	main()