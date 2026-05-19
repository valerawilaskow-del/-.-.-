#1
def square(num):
	return num ** 2
	
def cube(num):
	return num ** 3
	
def fun(num):
    sq = square(num)  # сначала возводим в квадрат
    cub = cube(sq)  # затем возводим результат в куб
    return cub
print(fun(10))
#2

def capitalize_string(text):
    """
    Проверяет тип переменной и, если это строка,
    возвращает её с заглавной буквы.
    Если не строка, возвращает сообщение об ошибке.
    """
    if isinstance(text, str):
        return text.capitalize()

def greet_user(name):
    """
    Приветствует пользователя по имени.
    Использует capitalize_string для форматирования имени.
    """
    formatted_name = capitalize_string(name)
    return f"Привет, {formatted_name}!"

# Примеры вызова:
print(greet_user("темир"))
print(greet_user("айдын"))
print(greet_user("алекс"))