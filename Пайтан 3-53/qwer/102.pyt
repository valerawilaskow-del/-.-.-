dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
res = dct.values()
print(res) 

dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
res=dct.values()
print(res)

dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
res = list(dct.keys())
print(res)

dct1 = {
	'a': 1,
	'b': 2,
	'c': 3
}

dct2 = {
	1: 'a',
	2: 'b',
	3: 'c'
}
dct1.update(dct2)
res = list(dct1.values())
print(res)


