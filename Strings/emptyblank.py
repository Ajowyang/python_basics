def is_empty_or_blank(str):
	for i in range(len(str)):
		if str[i] != '':
			return False
	return True

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
