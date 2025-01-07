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

def getCountry(name):
	if name == 'Alice':
		return countries[0]
	elif name == 'Francois':
		return countries[1]
	elif name == 'Inti':
		return countries[2]
	elif name == 'Monika':
		return countries[3]
	elif name == 'Sanyu':
		return countries[4]
	elif name == 'Yoshitaka':
		return countries[5]

country_dict = {
	'Alice': 	'USA',
	'Francois': 	'Canada',
	'Inti': 	'Peru',
	'Monika': 	'Germany',
	'Sanyu':	'Uganda',
	'Yoshitaka': 	'Japan',
}


print(getName('Japan'))
print(getCountry('Sanyu'))
print(country_dict['Monika'])
