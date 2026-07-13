"""Спринт 03, задание 01: базовые функции."""

# Задание 1.
# Напиши функцию greet(), которая печатает "Hello, Python!".
# Вызови функцию.
def greet():
    print("Hello, Python!")
greet()

# Задание 2.
# Напиши функцию greet_user(name), которая принимает имя и печатает приветствие.
# Пример: greet_user("Maxi") -> Hello, Maxi!
def greet_user(name):
    print("Hello,", name + "!")

greet_user("Maxi")
# Задание 3.
# Напиши функцию print_square(number), которая печатает квадрат числа.
# Пример: print_square(5) -> 25
def print_square(number):
    number = number ** 2
    print(number)
    

print_square(5)

# Задание 4.
# Напиши функцию show_product(name, price), которая печатает товар и цену.
# Пример: milk costs 10.00 PLN
def show_product(name, price):
    print(f"{name} costs {price:.2f} PLN")

show_product("milk", 12.00)




# Задание 5.
# Напиши функцию is_adult(age), которая печатает:
# - "Adult", если age >= 18
# - "Too young", если age < 18
def is_adult(age):
    if age >= 18:
        print("Adult")
    else:
        print("Too young")

is_adult(15)

# Задание 6.
# Спроси у пользователя имя и возраст.
# Используй функции из заданий 2 и 5.
name = input("What's your name? ")
age = int(input("What's your age? "))
greet_user(name)
is_adult(age)

