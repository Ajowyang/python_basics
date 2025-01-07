my_list = [6, 3, 0, 11, 20, 4, 17]
i = 0
while i<len(my_list):
	print(my_list[i])
	i+=1

for j in range(0, len(my_list)):
	print(my_list[j])
k = 0
while k < len(my_list):
	if my_list[k] % 2 == 0:
		print(my_list[k])
	k+=1	

for num in my_list:
	if num % 2 == 1:
		print(num)
