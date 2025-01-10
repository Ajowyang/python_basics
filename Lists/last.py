def last(lst):
	if lst:
		return lst[len(lst) - 1]
	else:
		return None

print(last([1,2,3,4]))
print(last([]))
print(last(['Earth', 'Moon', 'Mars']))  # Mars
