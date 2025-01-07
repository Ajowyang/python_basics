my_range = range(0, 25, 3)
print("1. ", my_range[6])

my_string = "Launch School"
print("2. ", my_string[my_string.find('c'):my_string.find('c')+6]) 

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}
print(pets["Dog"])
print(pets.get("Lizard"))
print(pets.get("Lizard", '<silence>'))

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

info = info.replace(':', '+')
print(info)

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]
stuff[1][3] = 606
print(stuff)

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']
print( 3 in numbers1)
print( 3 in numbers2)
print( 3 in numbers3)
print( 3 in numbers4)
print( 3 in numbers5)

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)
tuple_list = []
for i in range(0, 3):
	tuple_list.append((my_str[i], my_list[i], my_tuple[i], my_range[i]))
print(tuple_list)
