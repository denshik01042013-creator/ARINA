import random
import time

class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 40
        self.energy = 60
        self.happiness = 50
        self.age = 0

    def eat(self):
        print(f"{self.name} поїв 🍗")
        self.hunger -= 30
        self.energy += 5

    def sleep(self):
        print(f"{self.name} спить 😴")
        self.energy += 30
        self.hunger += 10

    def play(self):
        print(f"{self.name} грається 🎾")
        self.energy -= 20
        self.happiness += 20
        self.hunger += 15

    def normalize(self):
        self.hunger = max(0, min(100, self.hunger))
        self.energy = max(0, min(100, self.energy))
        self.happiness = max(0, min(100, self.happiness))

    def status(self):
        print(f"\nСтатус {self.name}:")
        print(f"Вік: {self.age}")
        print(f"Голод: {self.hunger}")
        print(f"Енергія: {self.energy}")
        print(f"Щастя: {self.happiness}")

        if self.hunger > 80:
            print(f"{self.name} дуже голодний 😿")
        if self.energy < 20:
            print(f"{self.name} дуже втомлений 😴")
        if self.happiness < 20:
            print(f"{self.name} сумний 😢")

    def live_day(self):
        self.age += 1

        action = random.choice([self.eat, self.sleep, self.play])
        action()

        self.hunger += 5
        self.energy -= 5
        self.happiness -= 2

        self.normalize()
        self.status()


cat = Cat("Барсик")

for day in range(10):
    print(f"\n--- День {day + 1} ---")
    cat.live_day()
    time.sleep(1)