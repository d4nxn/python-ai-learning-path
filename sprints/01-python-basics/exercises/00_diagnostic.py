"""Стартовая диагностика. Выполни без AI и не бойся ошибок."""

# 1. Создай переменные с именем, возрастом и городом.
name = "Maxi"
age = 20
city = "Kielce"

# 2. Выведи одну строку вида:
#    Меня зовут Максим, мне 20 лет, я живу в Кельце.

print(f"My name is {name}, I'm {age} years old, I live in {city}.")

# 3. Создай список из четырёх чисел и выведи только числа больше 3.
numbers = [3, 8, 1, 12]
for number in numbers:
    if number > 3:
        print(number)

# 4. Спроси у пользователя число и сообщи, положительное оно, отрицательное или ноль.
def is_positive():
    while True:
        try:
            chislo = int(input("What's the number? "))

            if chislo > 0:
                print("Your number is positive")
            elif chislo < 0:
                print("Your number is negative")
            else:
                print("Your number equals 0") 
            break
        except ValueError:
            print("Number is not an integer")
        

ispositive()
# 5. Напиши одним предложением в комментарии, какая часть была самой трудной.
# Сложнее всего было расставить пробелы чтобы все работало и еще я перепутал местами int и input

