#1
def func(num1, num2):
	'''Имя каждой функции должно точно отражать то, что функция делает.'''
	return num1 * num2
#2
def user(name):
	'''Имена функций должны быть глаголами.'''
	return 'bye, ' + name
#3
def get_num(num):
	'''Функция должна делать только то, что явно подразумевается её названием, и не делать другого.'''
	return str(num)
#4
def check(lst):
	'''Длинные функции лучше разбивать на ряд вспомогательных.'''
	sum = 0
	
	for el in lst:
		if el > 0:
			sum += el
		if el < 0:
			continue
		else:
			continue
			
	return sum