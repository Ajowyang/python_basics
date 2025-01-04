myAge=int(input())

def futureAge(age):
	print("You are " + str(age) + " years old.")
	for i in range(1, 5):
		print("In " + str(i*10) + " years, you will be " + str(age + (i*10)) + " years old.")
futureAge(myAge)
