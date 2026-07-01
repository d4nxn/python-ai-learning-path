"""Спринт 02, задание 04: отладка коллекций.

В файле намеренно есть ошибки.
Исправляй по одной, запускай файл после каждого исправления.
Рядом оставляй комментарий: тип ошибки, причина, исправление.
"""

products = ["milk", "bread", "apple"]
print(products[3])

prices = [10, 20, "30"]
total = 0
for price in prices:
    total += price
print(total)

user = {"name": "Maxi", "age": 20}
print(user["city"])

cart = []
cart += "milk"
print(cart)

limits = {"food": 500, "transport": 200}
category = input("Category: ")
print(limits[category])

