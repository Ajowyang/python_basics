def count_substrings(a, b):
	result = 0
	for i in range(len(a)):
		if a[i] == b[0]:
			if a[i:i+len(b)] == b:
				result += 1
	return result

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0
