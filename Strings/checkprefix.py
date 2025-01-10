def starts_with(str, sub):
	if str[0: len(sub)] == sub:
		return True
	else:
		return False

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True
