"""Переменные, типы, input и преобразования."""

# Задание 1.
# Спроси имя и любимую технологию. Выведи персональное сообщение через f-строку.
def info():
    name = input("What's your name? ")    
    tech = input("What's your favorite tech? ")
    print (f"Your name is {name} and your favorite tech is {tech}")

info()    
# Задание 2.
# Спроси возраст и выведи примерный год рождения.
# Подумай, почему результат input() нужно преобразовать.
age = int(input("What's your age? ")) 
year_born = 2026 - age
print(f"You were probably born in {year_born}")

# Задание 3.
# Спроси количество отработанных часов и ставку за час.
# Выведи зарплату с двумя цифрами после точки.
def paycheck():
    wage = float(input("What's your hourly wage? "))
    hours = float(input("How many hours did you worked in last month? "))
    total_pay = wage * hours
    print(f"You've earned {paycheck:.2f}$")

paycheck() 

# Задание 4.
# Создай по одной переменной типов str, int, float и bool.
# Выведи значение каждой переменной и результат type(...).

price = float(2.99)
surname = str("Coleman")
width = int(4)
single = bool(False)

print(f"chips' price is {price} and it's {type(price)}")
print(f"Your surname is {surname} and it's {type(surname)}")
print(f"width equals {width} and it's {type(width)}")
print(f"Are you single? {single} And it's {type(single)}")

# Задание 5 — эксперимент.
# Удали одно преобразование int() или float(), запусти программу и запиши ошибку.
# Затем верни исправление и объясни ошибку комментарием.
# TypeError: unsupported operand type(s) for -: 'int' and 'str'
# input всегда возвращает str, а нам нужен был возраст в виде int