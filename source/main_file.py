from time import sleep
from functools import wraps

print("Hello, World!!!")
sleep(1)

# декоратор
def my_dec(number: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"начало работы декоратора {number}")
            result = func(*args, **kwargs)
            print(f"конец работы декоратора {number}")
            return result
        return wrapper
    return decorator
            
@my_dec(5)
def func(value: int) -> int:
    print(f"работает функция: {func.__name__}")
    return value ** 2


def my_func(string: str) -> int:
    """возвращает кол-во гласных букв в строке"""
    predicate = lambda w: w in "aeyuio"
    return len(list(filter(predicate, string)))

def new_function(value: int) -> int:
    """новая функция"""
    result = value + value
    return result

print("конец")