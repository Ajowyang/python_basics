def find_integers(list):
	result = []
	for item in list:
		if type(item) is int:
			result.append(item)
	return result

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]


