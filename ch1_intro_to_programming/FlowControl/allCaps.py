myStr = input("Enter string: ")
def allCaps(str):
	if len(str) > 10:
		return str.upper()
	else:
		return str
print(allCaps(myStr))
