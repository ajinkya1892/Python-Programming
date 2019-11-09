# 3.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that
# numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

# importing functools for reduce()
import functools
arr = []
print "Entrer the no of elements"

num  = input(">")

print " Enther the numbers "

for i in range(0,num):
	number = input(">>")
	arr.append(number)

def Brk_check(num):
	if num >= 70 and num <= 90:
		return num

def IncTen(num):
	return num + 10

def Prdct(num1,num2):
	return num1*num2

Filtered_arr = list(filter(Brk_check,arr))
print("Filtered Data is : ",Filtered_arr)
Mapped_arr = list(map(IncTen,Filtered_arr))
print ("Mapped array is : ",Mapped_arr)
Reduced_arr = reduce(Prdct,Mapped_arr)
print ("Reduced array is : ",Reduced_arr)

print Reduced_arr

if __name__ == "__main()__":
	main()