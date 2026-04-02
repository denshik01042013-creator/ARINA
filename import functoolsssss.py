import functools

def robust_calculator(func):
    """Декоратор для обробки помилок та забезпечення стабільності калькулятора."""
    @functools.wraps(func)
    def wrapper(expression):
        try:
            result = func(expression)
            return f"Результат: {result}"
        
        except ZeroDivisionError:
            return "Помилка: Ділення на нуль неможливе!"
        
        except NameError:
            return "Помилка: Використано заборонені символи або змінні. Вводьте лише цифри та оператори (+, -, *, /)."
        
        except SyntaxError:
            return "Помилка: Некоректний вираз. Перевірте правильність написання."
        
        except Exception as e:
            return f"Сталася непередбачена помилка: {e}"
            
    return wrapper

@robust_calculator
def calculate(expression):
    return eval(expression)

if __name__ == "__main__":
    print(calculate("10 + 5 * 2"))    
    print(calculate("10 / 0"))       
    print(calculate("10 + hello"))    
    print(calculate("10 + (5 * )"))   