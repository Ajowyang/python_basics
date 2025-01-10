def extract_language(code):
        return code.split('_')[0]

def extract_region(code):
        return code.split('_')[1].split('.')[0]

def local_greet(code):
	country = extract_language(code)
	region = extract_region(code)
	match country:
		case 'en':
			if region == 'US':
				return 'Hi!'
			elif region == 'GB':
				return 'Hello!'
			elif region == 'AU':
				return 'Howdy!'
		case 'fr':
			return 'Salut!'
		case 'pt':
			return 'Ola!'
		case 'de':
			return 'Hallo!'
		case 'sv':
			return 'Hej!'
		case 'af':
			return 'Haai!'

#print(greet('en'))         # Hi!
#print(greet('fr'))         # Salut!
#print(greet('pt'))         # Olá!
#print(greet('de'))         # Hallo!
#print(greet('sv'))         # Hej!
#print(greet('af'))         # Haai!

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!
