# 5.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
# return Maximum number from that numbers. (You can also use normal functions instead of
# lambda functions).
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62


# importing functools for reduce()
import functools
arr = []
print "Entrer the no of elements"

num  = input(">")

print " Enther the numbers "

for i in range(0,num):
	number = input(">>")
	arr.append(number)

def Chk_Prime(num):
	if num > 1:
		for i in range(2, num):
			if (num % i) == 0:
				return False
				break
		else:
			return True
	else:
		return False

def Mul_by_2(num):
	return num*2

def MaxNum(num1,num2):
	max = 0
	if num1 > num2:
		return num1
	else:
		return num2

Filtered_arr = list(filter(Chk_Prime,arr))
print("Filtered Data is : ",Filtered_arr)
Mapped_arr = list(map(Mul_by_2,Filtered_arr))
print ("Mapped array is : ",Mapped_arr)
Reduced_arr = reduce(MaxNum,Mapped_arr)
print ("Reduced array is : ",Reduced_arr)

if __name__ == "__main()__":
	main()

