"""Условия и логические выражения."""

# Задание 1.
# Спроси число и выведи: положительное, отрицательное или ноль.

def lesson1():
    number = int(input("What's the number? "))
    if number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print("Number equals 0")

lesson1()

# Задание 2.
# Спроси возраст и наличие билета (yes/no).
# Разреши вход только пользователю не младше 18 лет с билетом.

def lesson2():
    age = int(input("How old are you? "))
    if age >= 18 and ticket():
        print("Access granted!")
    else:
        print("You are not welcome.")
    
    
    
def ticket():
    bilet = (input("Do you have a ticket? ")).lower()
    if bilet == "yes":
        return True
    else:
        return False

lesson2()

# Задание 3.
# Спроси сумму покупки.
# До 100 PLN скидка 0%, от 100 PLN скидка 5%, от 300 PLN скидка 10%.
# Выведи скидку и итоговую сумму.

def shopping():
    spent = int(input("How much is your total? "))
    percent = 0
    if spent < 100:
        print(f"Your discount is {percent}% and your total is {spent}zl")
    elif 300 > spent >= 100:
        percent = 5
        discount = spent * percent/100
        new_price = spent - discount
        print(f"Your discount is {percent}% and your total is {new_price}zl")
    else:
        percent = 10
        discount = spent * percent / 100
        new_price = spent - discount
        print(f"Your discount is {percent}% and your total is {new_price}zl")

shopping()


# Задание 4.
# Спроси логин и PIN. Сравни с заранее заданными значениями.
# Не сообщай отдельно, что именно было неправильным.

def lesson4():
    login = "mfmaxi"
    pin = "1025"
    entered_login = input("What's the login? ")
    entered_pin = input("What's the PIN? ")
    if login == entered_login and pin == entered_pin:
        print("Access granted!")
    else:
        print("Nice try.")

lesson4()
# Задание 5.
# Объясни комментариями разницу между =, ==, !=, >, >=, and, or и not.
# = присвает значение, == значит равно, != - не равно, > - больше, >= - больше либо равно, and - когда два условия выполняются, or - одно из условий выполняется, not - инвертирует значение (not True = False, not False = True)
