# 3.Write a program which accept N numbers from user and store it into List. Return Minimum
# number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5
import sys

arr = []
print "Entrer the no of elements"

num  = input(">")

print " Enther the numbers "

for i in range(0,num):
	number = input(">>")
	arr.append(number)

min = sys.maxint
for n in range(0,num):
	if arr[n] < min:
		min = arr[n]

print "Entered numbers are:"
print arr

print "Entered Minimum number is:"
print min