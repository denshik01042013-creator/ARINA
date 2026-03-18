import random

class Encryptor:
    def __init__(self, number):
        self.__original_value = number
        self.__operation_description = ""
        self.__result = self.__calculate()

    def __calculate(self):
        """Внутрішній метод, що обирає випадкову операцію та фіксує її крок"""
        rand_val = random.randint(2, 50)
        
        operations = [
            {"func": lambda x: x * rand_val, "desc": f"помножено на {rand_val}"},
            {"func": lambda x: x + rand_val, "desc": f"додано {rand_val}"},
            {"func": lambda x: x ** 2, "desc": "піднесено до квадрата"},
            {"func": lambda x: x - rand_val, "desc": f"віднято {rand_val}"}
        ]
        
        chosen = random.choice(operations)
        self.__operation_description = chosen["desc"]
        
        return chosen["func"](self.__original_value)

    def __str__(self):
        """Виводить результат та деталі 'секретного' обчислення"""
        return (f"Результат: {self.__result}\n"
                f"Як це сталося: Число {self.__original_value} було {self.__operation_description}.")

if __name__ == "__main__":
    user_input = int(input("Введіть число: "))
    cipher = Encryptor(user_input)
    
    print(cipher)