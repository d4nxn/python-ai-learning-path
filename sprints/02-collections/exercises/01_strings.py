"""Спринт 02, задание 01: строки.

Запускай файл после каждого задания.
Не используй AI для готового решения, сначала попробуй сам.
"""

# Задание 1.
# Спроси имя пользователя.
# Убери лишние пробелы по краям и выведи имя с большой буквы.
# Пример: "  maxi  " -> "Maxi"

name = input("What's your name? ")
name = name.strip().title()
print(f"Hello, {name}!")


# Задание 2.
# Спроси email.
# Приведи его к нижнему регистру и убери пробелы по краям.
# Если в email есть символ "@", выведи "Email accepted", иначе "Invalid email".
email = input("What's your email?")
email = email.strip().lower()
if "@" in email:
    print("Email accepted!")
else:
    print("Invalid email adress.")

# Задание 3.
# Дана строка:
# text = "python,ai,backend,llm"
# Разбей её на список слов через .split(",") и выведи каждое слово на отдельной строке.

text = "python,ai,backend,llm"
words = text.split(",")
for word in words:
    print(word)


# Задание 4.
# Спроси у пользователя короткое описание покупки.
# Замени все пробелы на дефисы.
# Пример: "green apple juice" -> "green-apple-juice"
item = input("What did you buy? ")
item = item.replace(" ", "-")
print(item)


# Задание 5.
# Дана строка:
# words = ["python", "is", "powerful"]
# Собери её в одну строку через пробел с помощью " ".join(words).
words = ["python", "is", "powerful"]
words = " ".join(words)
print(words)

# Задание 6.
# Спроси пароль.
# Если длина пароля меньше 8 символов, выведи "Too short".
# Иначе выведи "Password length accepted".
passw = input("What's the password? ")
if len(passw) >= 8:
    print("Password length accepted")
else:
    print("Too short")
