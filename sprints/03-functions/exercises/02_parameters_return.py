"""Спринт 03, задание 02: параметры и return."""

# Задание 1.
# Напиши функцию add(a, b), которая возвращает сумму двух чисел.
# Не печатай внутри функции, используй return.
def add(a,b):
    return a+b
print(add(2,3))

# Задание 2.
# Напиши функцию calculate_discount(total), которая:
# - возвращает total * 0.05, если total >= 200
# - возвращает 0, если total < 200
def calculate_discount(total):
    if total >= 200:
        return total * 0.05
    else:
        return 0
print(calculate_discount(200))


# Задание 3.
# Напиши функцию final_total(total), которая использует calculate_discount(total)
# и возвращает сумму после скидки.
def final_total(total):
    discount = calculate_discount(total)
    final = total - discount
    return final
    
print(final_total(400))


# Задание 4.
# Напиши функцию normalize_category(category), которая возвращает категорию
# без пробелов по краям и в нижнем регистре.
def normalize_category(category):
    category = category.lower().strip()
    return category

print(normalize_category("ClRASFASFASasda2"))


# Задание 5.
# Напиши функцию get_price_with_tax(price, tax_percent), которая возвращает цену с налогом.
# Пример: price=100, tax_percent=23 -> 123
def get_price_with_tax(price, tax_percent):
    full_price = price * (1 + tax_percent / 100)
    return full_price
print(get_price_with_tax(20,23))


# Задание 6.
# Спроси у пользователя сумму покупки.
# Выведи скидку и итог через функции из заданий 2 и 3.
total = float(input("What's the total? "))
print(calculate_discount(total))
print(final_total(total))

