# 4.Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

import sys

arr = []
print "Enter the no of elements"

num  = input(">")

print " Enter the numbers "

for i in range(0,num):
	number = input(">>")
	arr.append(number)

num_choice  = input("Enter the number for which freq to be found : ")
counter = 0
for j in arr:
	if j == num_choice:
		counter+=1

print("The frequency of %d is : %d  "%(num_choice,counter))
