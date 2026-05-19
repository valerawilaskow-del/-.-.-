dct1 = {
	'a': 1,
	'b': 2,
	'c': 3
}

dct2 = {
	'x': 4,
	'y': 5,
	'z': 6
}
dct1 .update(dct2)
print(dct1)

dct3 = {
	'3': 'c',
	'4': 'd',
	'5': 'e'
}

dct4 = {
	'1': 'a',
	'2': 'b'
}
dct4 .update(dct3)
print(dct4)


dct5 = {
    'a': 1, 
    'b': 2, 
    'c': 3
}
dct6 = {
    'x': 4, 
    'y': 5, 
    'z': 6
}
merged_dict = dct5.copy()  
merged_dict.update(dct6)
result_list = list(merged_dict.items())
print(merged_dict)  
print(result_list) 

dct7 = {
	'a': 1,
	'b': 2,
	'c': 3
}

dct8 = {
	'd': 4,
	'e': 5,
	'f': 6
}

dct9 = {
	'j': 7,
	'h': 8,
	'i': 9
}
dct7.update(dct8)
dct7 .update(dct9)
print(dct7)

