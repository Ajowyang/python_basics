num = int(input("Enter a number: "))
def number_range(n):
	if (n <= 50) and (n >= 0):
		print("the value is between 0 and 50 (inclusive)")
	elif (n <= 100) and (n >= 51):
		print("the value is between 51 and 100 (inclusive)")
	elif n > 100:
		print("the value is greater than 100")
	else:
		print("the value is less than 0")
number_range(num)
