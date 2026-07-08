"""Мини-проект второй недели: анализатор покупок.

Сначала прочитай README.md в этой папке.
Реализуй требования самостоятельно.
"""
print("Hello, user.")
items = []
total = 0
items_count = 0


while True:
    name = input("What you buying? ")
    if name == "stop":
        break

    while True:
        try:
            price = float(input("What's the price? "))

            if price <= 0:
                # Ошибка была здесь: без continue программа могла идти дальше,
                # хотя цена неправильная. continue снова спрашивает цену.
                print("Price must be positive. ")
                continue

            # Ошибка была здесь: после правильной цены нужно выйти из цикла цены.
            # break завершает только внутренний while True с ценой.
            break
        except ValueError:
            # Если введено "abc", float(...) падает, а переменная price не создаётся.
            # Поэтому после ValueError нельзя переходить к созданию товара.
            print("Price must be a number.")

    # Ошибка была в отступах: category нельзя спрашивать внутри цикла цены.
    # Сначала добиваемся правильной цены, потом спрашиваем категорию.
    category = input("What's the category? ").strip().lower()

    # item создаётся внутри цикла товаров, но после name, price и category.
    item = {
        "name": name,
        "price": price,
        "category": category
    }

    total += price
    items_count += 1

    items.append(item)

print(f"You've bought: {items}, your total is {total:.2f} and you've bought {items_count} items")
categories = set()
for item in items:
    category = item["category"]
    categories.add(category)
print(f"Categories: {categories}")

category_totals = {}
for item in items:
    category = item["category"]
    price = item["price"]

    if category not in category_totals:
        category_totals[category] = 0

    category_totals[category] += price

print("Totals by category:")
for category, total in category_totals.items():
    print(f"{category}: {total:.2f}")

      
