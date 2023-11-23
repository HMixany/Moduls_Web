import asyncio
from time import sleep, time
from faker import Faker

fake = Faker('uk-UA')

# Awaitable -> Coroutine
# Awaitable -> Future -> Task


async def async_get_user_from_db(uuid: int):
    await asyncio.sleep(0.5)                    # імітація запроса до БД
    return {'id': uuid, 'username': fake.user_name(), 'email': fake.email()}


async def main():
    users = []
    for i in range(1, 26):
        task = asyncio.create_task(async_get_user_from_db(i))        # створюємо таску і додаєм виконання корутини в неї
        users.append(task)                             # збираємо таски у список
    result = await asyncio.gather(*users)              # передамо функції gather список курутин через кому, та отримаємо
                                                       # список результатів
    return result



if __name__ == '__main__':
    start = time()
    users = asyncio.run(main())
    print(users)
    print(time() - start)