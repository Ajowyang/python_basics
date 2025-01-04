names = ['Alice', 'Francois', 'Inti', 'Monika', 'Sanyu', 'Yoshitaka']
countries = ['USA', 'Canada', 'Peru', 'Germany', 'Uganda', 'Japan']

def getName(country):
	if country == 'USA':
		return names[0]
	elif country == 'Canada':
		return names[1]
	elif country == 'Peru':
		return names[2]
	elif country == 'Germany':
		return names[3]
	elif country == 'Uganda':
		return names[4]
	elif country == 'Japan':
		return names[5]

print(getName('Japan'))
