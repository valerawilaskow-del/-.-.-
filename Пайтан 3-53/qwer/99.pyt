dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}

print(dct.get(4))

dct = {
	1: 'a',
	2: 'b',
	3: 'c',
	4: 'd'
}

print(dct.get('3'))

dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print(dct.get('w','!'))