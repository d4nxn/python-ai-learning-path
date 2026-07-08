"""Спринт 02, задание 04: отладка коллекций.

В файле намеренно есть ошибки.
Исправляй по одной, запускай файл после каждого исправления.
Рядом оставляй комментарий: тип ошибки, причина, исправление.
"""

products = ["milk", "bread", "apple"]
print(products[2]) #Счёт идет от нуля, а не от единицы, исправил products[3] на products[2]

prices = [10, 20, 30]#30 было указано не как int, а как str, поэтому шла ошибка, нельзя добавть str к int
total = 0
for price in prices:
    total += price
print(total)

user = {"name": "Maxi", "age": 20}
print(user["name"])#не было описано city, изменил на name

cart = []
cart.append("milk")#в списки добавляем с помощью append, а не +=
print(cart)

limits = {"food": 500, "transport": 200}
choice = input("What's the category? ")
limit = limits.get(choice)
if limit is not None:
    print(limit)
else:
    print("No limit for this category.")


#Изменил структуру запроса, при вводе несуществующей категории вылазила ошибка, а теперь нет
