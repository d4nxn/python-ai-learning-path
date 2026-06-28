"""Циклы for и while."""

# Задание 1.
# Выведи числа от 1 до 20 с помощью for и range().

def ranger():
    for i in range(1, 21):
        i += 1
        print(i)
ranger()
# Задание 2.
# Выведи только чётные числа от 2 до 30.
def even():
    for i in range(2, 31):
        if i % 2 == 0:
            print(i)

even()


# Задание 3.
# Дан список prices = [12.5, 8.0, 19.99, 3.5].
# Самостоятельно посчитай сумму через цикл, не используя sum().

prices = [12.5, 8.0, 19.99, 3.5]
def sum_up():
    summa = 0
    for price in prices:
        summa += price
    print(f"{summa:.2f}")

sum_up()

# Задание 4.
# Дай пользователю максимум три попытки ввести правильный PIN.
# После успеха останови цикл. После трёх ошибок сообщи о блокировке.

def login():
    pin = 1025

    for attempt in range(3):
        pin_entered = int(input("What's the PIN? "))
        if pin_entered == pin:
            print("Access granted!")
            break
    else:
        print("You are blocked.")

login()


# Задание 5.
# Принимай числа, пока пользователь не введёт stop.
# После завершения выведи количество чисел и их сумму.
def stopping():
    summ = 0
    count = 0 
    while True:
        users = input("What's the number? ")
        if users == "stop":
            break
        else:
            number = int(users)
            summ += number
            count += 1
    print(f"Summa: {summ}, number of numbers: {count}")

stopping()

