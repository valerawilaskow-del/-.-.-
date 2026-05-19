dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print(len(dct))

dct1 = { 
    'a': 12, 
    'b': 34, 
    'c': 56, 
    'd': 78, 
    'e': 90
}
dct2 = {}
dct2[str(dct1)] = dct1
print(dct2)
