my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

my_list_len = len(my_list)
i = 0

while i < my_list_len:
	list = my_list[i]
	list_len = len(list)
	j = 0
	while j < list_len:
		if list[j] % 2 == 0:
			print(list[j])
		j+=1
	i+=1


