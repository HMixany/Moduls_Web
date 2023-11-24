import asyncio
from typing import AsyncIterator, Any
from timing import async_timed

from faker import Faker


fake = Faker('uk-UA')


async def get_user_from_db(uuid: int):
    await asyncio.sleep(0.5)                    # імітація запроса до БД
    return {'id': uuid, 'username': fake.user_name(), 'email': fake.email()}


async def get_users(uuids: list[int]) -> AsyncIterator:
    for uuid in uuids:                                 # асинхронний ітератор
        yield get_user_from_db(uuid)


@async_timed()
async def main(users: AsyncIterator):
    users_ = [user async for user in users]
    result = await asyncio.gather(*users_)
    return result


if __name__ == '__main__':
    r = asyncio.run(main(get_users([1, 2, 3])))
    print(r)