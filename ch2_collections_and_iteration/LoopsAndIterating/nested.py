my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for list in my_list:
	for num in list:
		if num % 2  == 0:
			print(num)
even_odd=[]
for list in my_list:
	for num in list:
		if num % 2 == 0:
			even_odd.append("even")
		else:
			even_odd.append("odd")
print(even_odd)
