dct = {'x': '1', 'y': '2', 'z': '3'}
result = sum(int(value)**2 for value in dct.values())
print(result)

dct1 = {
    '1': 12,
    '2': 24,
    '3': 36
}
dct2 = {
    'a': '3',
    'b': '6',
    'c': '9'
}
sum_dct1 = sum(dct1.values())           
sum_dct2 = sum(map(int, dct2.values())) 
result = sum_dct1 - sum_dct2            
print(result)       


dct = {1: '4', 2: '5', 3: '6'}
new_dct = {key: str(value) for key, value in dct.items()}
print(new_dct)

dct = {'x': 1, 'y': 2, 'z': 3}
result = ''.join(str(value) for value in dct.values())
print(result)

dct = {
    'y': 2026,  
    'm': 2,
    'd': 4
}
formatted_date = f"{dct['y']}-{dct['m']:02}-{dct['d']:02}"
print(formatted_date)