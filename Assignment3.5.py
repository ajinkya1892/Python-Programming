# 5.Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54 (13 + 5 + 7 +2 + 5)
from MarvellousNum import *
def ListPrime(brr):
	tot=0
	for num in brr:
		if ChkPrime(num):
			# print num
			tot = tot + num
	return tot

arr = []
print "Enter the no of elements"

num  = input(">")

print " Enter the numbers "

for i in range(0,num):
	number = input(">>")
	arr.append(number)

total = ListPrime(arr)
print ("Total of all prime is : ",total)



