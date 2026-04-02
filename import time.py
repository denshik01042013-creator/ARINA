import time
import functools
import unittest

def execution_time_decorator(func):
    """Декоратор для вимірювання часу роботи."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        execution_time = end_time - start_time
        print(f"\n[LOG] Функція '{func.__name__}' виконана за {execution_time:.6f} сек.")
        return result, execution_time
    return wrapper

@execution_time_decorator
def slow_function(seconds):
    """Імітація затримки."""
    time.sleep(seconds)
    return "Успішно"



class TestMyCode(unittest.TestCase):
    
    def test_timer_accuracy(self):
        """Тест: чи відповідає виміряний час заданій затримці?"""
        delay = 0.3
        result, exec_time = slow_function(delay)
        
        self.assertEqual(result, "Успішно")
        self.assertAlmostEqual(exec_time, delay, delta=0.05)

    def test_output_format(self):
        """Тест: чи повертає декоратор правильну структуру даних?"""
        output = slow_function(0.1)
        self.assertIsInstance(output, tuple)
        self.assertEqual(len(output), 2)



if __name__ == '__main__':
    unittest.main()