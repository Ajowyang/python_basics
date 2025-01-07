my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = {	x : len(x)
	 	for x in my_set
		if len(x) % 2 == 1
}
print(my_dict)
