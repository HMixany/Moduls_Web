import asyncio
from time import sleep, time
from faker import Faker

fake = Faker('uk-UA')


def get_user_from_db(uuid: int):
    sleep(0.5)
    return {'id': uuid, 'username': fake.user_name(), 'email': fake.email()}


async def async_get_user_from_db(uuid: int):
    await asyncio.sleep(0.5)                    # імітація запроса до БД
    return {'id': uuid, 'username': fake.user_name(), 'email': fake.email()}


async def main():
    users = []
    for i in range(1, 26):
        users.append(async_get_user_from_db(i))        # заповнимо список корутинами
    result = await asyncio.gather(*users)              # передамо функції gather список курутин через кому, та отримаємо
                                                       # список результатів
    return result



if __name__ == '__main__':
    start = time()
    for i in range(1, 26):
        user = get_user_from_db(i)
        print(user)
    print(time() - start)

    start = time()
    users = asyncio.run(main())
    print(users)
    print(time() - start)