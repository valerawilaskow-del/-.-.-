dct = {
	'x': 1,
	'y': 2,
	'z': 3
}       
print(dct['x'])
print(dct['y'])
print(dct['z'])

dct1 = {
	'a': 1,
	'b': 2,
	'c': 3
}
print(dct1['b'])

dct2 = {
	'x': 1,
	'y': 2,
	'z': 3
}
key = 'x'
print(dct[key])     


dct3 = {
    'a': 5, 
    'b': 10, 
    'c': 15
}
total_sum = 0
for value in dct3.values():
    print(value)  
    total_sum += value  
print("Сумма всех значений:", total_sum)

dct4 = {
    1: 'a',
    2: 'b',
    3: 'c'
}
result = ''.join(dct4.values())
print(result)  
