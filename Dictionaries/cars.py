cars = {
'car': {
	'type': 'sedan',
	'color': 'blue',
	'year': 2003,
	},
'truck': {
	'type': 'pickup',
	'color': 'red',
	'year': 1998,
	},
}


print(cars)


car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}
print(list(car))
print([[key, value] for key, value in car.items()])
