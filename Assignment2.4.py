"""Write a program which accept one number form user and return addition of its factors."""

def factors_of_num(n):
	lst=[]
	for i in range(1,n):
		if n%i==0:
			# print(i)
			lst.append(i)
	return (lst)

def sum_of_arr(arr):
	return sum(arr)

factors = factors_of_num(12)
# print(factors)
print(sum_of_arr(factors))
