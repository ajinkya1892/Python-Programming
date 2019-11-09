# 2.Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56

arr = []
print "Entrer the no of elements"

num  = input(">")

print " Enther the numbers "

for i in range(0,num):
	number = input(">>")
	arr.append(number)

max = 0
for n in range(0,num):
	if arr[n] > max:
		max = arr[n]

print "Entered numbers are:"
print arr

print "Entered Maximum number is:"
print max