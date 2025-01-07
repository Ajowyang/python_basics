import random

highest = 10


while True:
	number = random.randint(0, highest)
	print(number)
	if number == highest:
		break

