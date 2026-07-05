"""Спринт 02, задание 02: списки."""

# Задание 1.
# Создай пустой список products.
# В цикле спрашивай название товара, пока пользователь не введёт stop.
# Каждый товар добавляй в список через .append().
# После stop выведи список.

products = []
while True:
    product = input("What you buying? ")
    if product == "stop":
        print(f"You Have Bought: {products} ")
        break
    else:
        products.append(product)




# Задание 2.
# Даны цены:
# prices = [10.5, 20, 7.99, 100]
# Через цикл посчитай общую сумму без sum().
prices = [10.5, 20, 7.99, 100]
total = 0
for price in prices:
    total += price
print (total)



# Задание 3.
# Для списка prices из задания 2 выведи только цены больше 15.
for price in prices:
    if price > 15:
        print(price)

# Задание 4.
# Даны товары:
# products = ["milk", "bread", "milk", "apple"]
# Посчитай, сколько раз встречается "milk", без использования .count().
products = ["milk", "bread", "milk", "apple"]
amount = 0
for product in products:
    if product == "milk":
        amount += 1
print(f"You have bought {amount} cartons of milk")
# Задание 5.
# Спроси у пользователя 5 чисел.
# Добавь их в список.
# После этого выведи:
# - сам список;
# - самое большое число;
# - самое маленькое число.
# Можно использовать max() и min().

numbers = []
for users_input in range(5):
    number = int(input("What is the number? "))
    numbers.append(number)
print(f"You entered {numbers}.")
print(f"lowest number is: {min(numbers)}")
print(f"Highest number is: {max(numbers)}")


# Задание 6.
# Даны товары:
# cart = ["milk", "bread", "apple"]
# Спроси, какой товар удалить.
# Если товар есть в списке — удали его и выведи обновлённый список.
# Если товара нет — выведи "Item not found".
cart = ["milk", "bread", "apple"]

item = input("What you deleting? ")
if item in cart:
    cart.remove(item)
    print(cart)
else:
    print("Item not found")


