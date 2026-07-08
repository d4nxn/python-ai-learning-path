"""Спринт 02, задание 03: словари и множества."""

# Задание 1.
# Создай словарь user с ключами:
# name, age, city.
# Выведи каждое значение отдельной строкой.
user = {
    'name': 'Belarus',
    'age': 1200,
    'city': 'Minsk'
}
for value in user.values():
    print(value)


# Задание 2.
# Спроси у пользователя категорию расхода.
# Есть словарь:
# limits = {"food": 500, "transport": 200, "fun": 150}
# Если категория есть в словаре, выведи лимит.
# Если нет — выведи "No limit for this category".
# Используй .get().


limits = {
    'food': 500,
    'transport': 200,
    'fun': 150
}
choice = input("What's the category? ")
limit = limits.get(choice)
if choice in limits:
    print(limit)
else:
    print("No limit for this category.")


    
# Задание 3.
# Даны транзакции:
# transactions = [
#     {"category": "food", "amount": 25},
#     {"category": "transport", "amount": 10},
#     {"category": "food", "amount": 40},
# ]
# Посчитай общую сумму расходов.

transactions = [
    {"category": "food", "amount": 25},
    {"category": "transport", "amount": 10},
    {"category": "food", "amount": 40},
 ]

summa = 0
for transaction in transactions:
    summa += transaction["amount"]
print(summa)

# Задание 4.
# Для transactions из задания 3 посчитай сумму только по категории "food".
food_total = 0
for transaction in transactions:
    if transaction["category"] == "food":
        food_total += transaction["amount"]
print(food_total)

# Задание 5.
# Даны категории:
# categories = ["food", "food", "transport", "fun", "transport"]
# Создай множество уникальных категорий и выведи его.
categories = ["food", "food", "transport", "fun", "transport"]
print(set(categories))


# Задание 6.
# Спроси у пользователя 5 слов.
# Сохрани только уникальные слова через set.
# Выведи количество уникальных слов.
words = set()
for _ in range(5):
    users = input("What's the word? ")
    if users not in words:
        words.add(users)
print(len(words))
