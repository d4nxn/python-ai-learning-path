"""Спринт 03, задание 04: отладка функций.

В файле намеренно есть ошибки.
Исправляй по одной. Рядом оставляй комментарий: тип ошибки, причина, исправление.
"""

def greet(name)
    print(f"Hello, {name}")


def add(a, b):
    result = a + b


total = add(10, 20)
print(total)


def calculate_total(items):
    total = 0
    for item in items:
        total += item["amount"]
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


if is_positive:
    print("Positive")

