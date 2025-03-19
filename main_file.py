from time import sleep
from functools import wraps

for i in range(1, 3):
    print(i)
    sleep(1)

print("обновление другим разработчиком")
"""еще добавили другие разработчики"""

print("Hello, World!!!")
sleep(1)

print("добавили еще")

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

if __name__ == "__main__":
    result = func(value=10)
    print(result)