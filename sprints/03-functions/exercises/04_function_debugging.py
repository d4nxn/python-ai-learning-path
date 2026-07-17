"""Спринт 03, задание 04: отладка функций.

В файле намеренно есть ошибки.
Исправляй по одной. Рядом оставляй комментарий: тип ошибки, причина, исправление.
"""

def greet(name): #SyntaxError: не было двоеточия
    print(f"Hello, {name}")


def add(a, b):
    result = a + b
    return result # Logical error - function were returning None instead of result

total = add(10, 20)
print(total)


def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"]#KeyError: no "amount" value in products, was replaced for "price"
    return total


products = [
    {"name": "milk", "price": 10},
    {"name": "bread", "price": 5},
]

print(calculate_total(products))


def is_positive(number):
    if number > 0:
        return True
    else:
        return False


if is_positive(3):  # Logical error: checked the function object instead of its return value; added a call with an argument
    print("Positive")

