"""6.Write a program which accept number from user and check whether that number is positive or
negative or zero.
Input : 11 Output : Positive Number
Input : -8 Output : Negative Number
Input : 0 Output : Zero"""

def sign_int(n):
	if n>0:
		print("Positive Number")
	elif n<0:
		print("Negative Number")
	else:
		print("Zero")

sign_int(11)
sign_int(-8)
sign_int(0)