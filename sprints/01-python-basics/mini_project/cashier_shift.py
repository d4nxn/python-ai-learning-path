"""Мини-проект первой недели: помощник кассира.

Сначала прочитай README.md в этой папке. Реализуй требования самостоятельно.
"""
def get_positive_number(question):
    while True:
        try:
            number = float(input(question))

            if number > 0:
                return number
            else:
                print("Number must be positive")
        except ValueError:
            print("Input must be a number")

print("Hello, cashier.")
# Шаг 1. Создай список товаров и переменную для общей суммы.

# Шаг 2. Напиши цикл добавления товаров до команды stop.

products = []
total = 0
positions = 0
while True:
    items = input("What you buying? ")
    if items == "stop":
        if total >= 200:
            discount = total * 5/100
        else:
            discount = 0
        final_total = total - discount
        print(f"You have in your cart: {products}")
        print(f"Items: {positions}, Total: {total:.2f}, Discount: {discount:.2f}")
        print(f"Final total: {final_total:.2f}")
        break
    else:
        price = get_positive_number("What's the price? ")
        total += price
        products.append(items)
        positions += 1
    
# Шаг 3. Проверь цену и обработай ValueError.

# Шаг 4. Рассчитай скидку.

# Шаг 5. Выведи понятный итоговый чек.

