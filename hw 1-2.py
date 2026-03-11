import random

#Ім'я та вік
name = input("Введіть ваше ім'я: ")
age = input("Введіть ваш вік: ")
print(f"Привіт {name}, тобі {age}!")

print("\n------------------\n")

#Перевірка віку
age = int(input("Введіть ваш вік: "))
if age > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")

print("\n------------------\n")

#Гра вгадай число
secret_number = random.randint(1, 10)

print("Гра 'Вгадай число'")
print("Я загадав число від 1 до 10. У тебе є 3 спроби.")

for attempt in range(3):
    guess = int(input("Введи число: "))

    if guess == secret_number:
        print("Вітаю! Ти вгадав!")
        break
    elif guess > secret_number:
        print("Менше")
    else:
        print("Більше")

    if attempt == 2:
        print(f"Спроби закінчились. Загадане число було {secret_number}")

print("\n------------------\n")

#Вивід чисел від "з" до "по"
start = int(input("Введіть число 'з': "))
end = int(input("Введіть число 'по': "))

for i in range(start, end + 1):
    print(i)

print("\n------------------\n")

#Оцінка студента
points = int(input("Введіть кількість балів (0-100): "))

if 0 <= points <= 49:
    print("Незадовільно")
elif 50 <= points <= 69:
    print("Задовільно")
elif 70 <= points <= 89:
    print("Добре")
elif 90 <= points <= 100:
    print("Відмінно")
else:
    print("Невірне значення балів")