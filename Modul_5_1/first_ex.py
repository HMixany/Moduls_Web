"""
Асинхронність для виконання IO Bound задач (але не всі модулі та пакети підтримують асинхронність і тоді multithreding)
Якщо паралелить важкі обчислення - multiprocesing
Функція яка має async/await є coroutine
"""
import asyncio
import requests


async def baz():               # async оголошує функцію асинхронною, та очикує в тілі функції await
    print('Це буде виконано відразу')
    await asyncio.sleep(1)           #
    print('А це виконається після того як відробе функція requests')
    return True


async def main():
    result = baz()            # виклик coroutine поверне об'єкт
    print(result)
    result = await result
    print(result)
    return result


if __name__ == '__main__':
    result = asyncio.run(main())
    print(result)

