"""Исправь фрагменты по одному. Сейчас в файле намеренно есть ошибки."""

# Правила:
# 1. Запускай файл после каждого исправления.
# 2. Возле исправленного места напиши: тип ошибки, причина, исправление.
# 3. Не переписывай всё сразу с помощью AI.

name = input("What is your name? ") #не была закрыта скобка
print(f"Hello, {name}!")

age = int(input("How old are you? "))#добавили тип input'а
next_age = age + 1
print(f"Next age: {next_age}")

price = float(input("Price: "))
if price > 0:
    print("Accepted")#не было нужных пробелов
else:
    print("Price must be positive")

numbers = [1, 2, 3, 4]
for number in numbers:
    if number > 2: #не было двоеточия
        print(number)


