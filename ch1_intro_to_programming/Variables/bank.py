myBalance = 1000.00
def compoundFive(balance):
	for i in range(0, 5):
		balance *=1.05
	return balance
print(compoundFive(myBalance))
