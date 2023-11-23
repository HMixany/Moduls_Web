import asyncio
from time import sleep, time
from faker import Faker

fake = Faker('uk-UA')

# Awaitable -> Coroutine
# Awaitable -> Future -> Task


async def async_get_user_from_db(uuid: int, future: asyncio.Future):
    await asyncio.sleep(0.5)                    # імітація запроса до БД
    future.set_result({'id': uuid, 'username': fake.user_name(), 'email': fake.email()})


def make_request(uuid: int) -> asyncio.Future:
    future = asyncio.Future()
    asyncio.create_task(async_get_user_from_db(uuid, future))
    return future


async def main():
    users = []
    for i in range(1, 26):
        users.append(make_request(i))                             # збираємо ф'ючерси у список
    print(users)
    print([user.done() for user in users])
    result = await asyncio.gather(*users)              # передамо функції gather список ф'ючерсів через кому, та отримаємо
                                                       # список результатів
    print([user.done() for user in users])
    return result



if __name__ == '__main__':
    start = time()
    users = asyncio.run(main())
    print(users)
    print(time() - start)