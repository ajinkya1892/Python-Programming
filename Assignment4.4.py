# 4.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

# importing functools for reduce()
import functools
arr = []
print "Entrer the no of elements"

num  = input(">")

print " Enther the numbers "

for i in range(0,num):
	number = input(">>")
	arr.append(number)

def Chk_Even(num):
	if num % 2 == 0:
		return True

def Sqr(num):
	return num*num

def Summation(num1,num2):
	return num1+num2

Filtered_arr = list(filter(Chk_Even,arr))
print("Filtered Data is : ",Filtered_arr)
Mapped_arr = list(map(Sqr,Filtered_arr))
print ("Mapped array is : ",Mapped_arr)
Reduced_arr = reduce(Summation,Mapped_arr)
print ("Reduced array is : ",Reduced_arr)

print Reduced_arr
