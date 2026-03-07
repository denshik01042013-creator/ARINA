name = input("Як тебе звати? ")
age = input("Скільки тобі років? ")
print(f"Привіт {name}, тобі {age}!")

age = int(age)
if age > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")
