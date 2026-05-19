#задание 1

def student_info(name, famil, course):
    name = name.capitalize()
    surname = famil.upper()
    print(f"Имя: {name}, Фамилия: {surname}, Курс: {course}")
name = "Temri"
surname = "Lamazhaa"
course = 2
student_info(name, surname, course)

#задание 2

def pl(a, b):
    return a * b
print(pl(3, 4))

#задание 3

def kor(text):
    return text
res = kor('hello')
print(res)

#задание 4

def number(num1, num2):

    if num1 > num2:
        print(f"{num1} > {num2}")
    elif num1 < num2:
        print(f"{num1} < {num2}")
    else:
        print(f"{num1} = {num2}")
print(number(5,5))

#задание 5

def convert(text):
 if isinstance(text, (int, float)):
        return str(text)
 return text
print(convert('rrr'))

#задание 6

def numbers(limit):
    numbers = []
    for num in range(2, limit + 1, 2):  # начинаем с 2, шаг 2
        numbers.append(num)
    return numbers
print(numbers(14))

#задание 7

def key(users):
    for name, age in users.items():
        print((name, age))
users = {"Temir": 18, "Aidyn": 17, "Stas": 18}
key(users)

#задание 8

def week(day_number):
    days = [
        "Понедельник", "Вторник", "Среда",
        "Четверг", "Пятница", "Суббота", "Воскресенье"
    ]
    if 1 <= day_number <= 7:
        return days[day_number - 1]
    else:
        return "Ошибка: введите число от 1 до 7"
print(week(2))