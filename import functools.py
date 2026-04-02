import functools

def robust_calculator(func):
    """Декоратор для обробки помилок та забезпечення стабільності калькулятора."""
    @functools.wraps(func)
    def wrapper(expression):
        try:
            # Виконуємо обчислення через оригінальну функцію
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

# Оригінальна функція з завдання
@robust_calculator
def calculate(expression):
    return eval(expression)

# --- Приклади використання ---
if __name__ == "__main__":
    print(calculate("10 + 5 * 2"))    # Коректний вираз
    print(calculate("10 / 0"))        # Ділення на нуль
    print(calculate("10 + hello"))    # Невідома змінна
    print(calculate("10 + (5 * )"))   # Синтаксична помилка