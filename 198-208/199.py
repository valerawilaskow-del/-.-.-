#1
def func(num1):
	print(num1 ** 2)
func(3)
#2
def func2(num1, num2):
	print(num1 * num2)
func2(9, 3)
#3
def func3(num):
	if num % 2 == 0:
		print('четное')
	else:
		print('нечетное')
func3(3)
#4

def func4(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total
res = func4([1, 2, 3])
print(res)