"""Спринт 03, задание 03: функции со списками и словарями."""

# Задание 1.
# Напиши функцию count_items(items), которая принимает список и возвращает его длину.
items = [
    {"name": "milk", "price": 10, "category": "food"},
    {"name": "bread", "price": 5, "category": "food"},
    {"name": "fluid", "price": 12, "category": "liquids"},
 ]
def count_items(items):
    return len(items)




# Задание 2.
# Напиши функцию calculate_total(items), которая принимает список словарей товаров
# и возвращает общую сумму цен.
#
# items = [
#     {"name": "milk", "price": 10, "category": "food"},
#     {"name": "bread", "price": 5, "category": "food"},
# ]
def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"]
    return total



# Задание 3.
# Напиши функцию get_unique_categories(items), которая возвращает set категорий.
def get_unique_categories(items):
    categories = set()
    for item in items:
        categories.add(item["category"])
    return categories
        




# Задание 4.
# Напиши функцию calculate_category_totals(items), которая возвращает словарь:
# категория -> сумма по категории.
def calculate_category_totals(items):
    categories_total = {}
    for item in items:
        category = item["category"]
        price = item["price"]
        if category not in categories_total:
            categories_total[category] = 0
        categories_total[category] += price
    return categories_total




# Задание 5.
# Напиши функцию find_expensive_items(items, min_price), которая возвращает список
# товаров дороже min_price.
def find_expensive_items(items, min_price):
    exp_items = []
    for item in items:
        if item["price"] > min_price:
            exp_items.append(item)
    return exp_items



# Задание 6.
# Создай тестовый список товаров и вызови все функции выше.
print(count_items(items))
print(calculate_total(items))
print(get_unique_categories(items))
print(calculate_category_totals(items))
print(find_expensive_items(items, 10))
