# coding=utf-8
"""Write a program which contains one function named as ChkNum() which accept one
parameter as number. If number is even then it should display “Even number” otherwise
display “Odd number” on console.
Input : 11 Output : Odd Number
Input : 8 Output : Even Number"""

def ChkNum(n):
	if (n%2) != 0 :
		print("Odd Number")
	else:
		print("Even Number")

ChkNum(11)
ChkNum(8)