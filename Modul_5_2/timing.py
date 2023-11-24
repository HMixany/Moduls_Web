'''
Асинхронний декоратор для асинхронних функцій. Виміроє час виконання coroutine
'''
from functools import wraps
import time
from typing import Callable, Any


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'Виконується {func.__name__} з аргументами {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func.__name__} завершила виконання за {total:.4f} с')
        return wrapped
    return wrapper


def sync_timed():
    def wrapper(func):
        @wraps(func)
        def wrapped(*args, **kwargs) -> Any:
            print(f'Виконується {func.__name__} з аргументами {args} {kwargs}')
            start = time.time()
            try:
                return func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func.__name__} завершила виконання за {total:.4f} с')
        return wrapped
    return wrapper