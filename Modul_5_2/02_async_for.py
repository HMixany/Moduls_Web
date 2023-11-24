import asyncio
from typing import Iterable, Awaitable, Coroutine, Any
from timing import async_timed

from faker import Faker


fake = Faker('uk-UA')


async def get_user_from_db(uuid: int):
    await asyncio.sleep(0.5)                    # імітація запроса до БД
    return {'id': uuid, 'username': fake.user_name(), 'email': fake.email()}


async def get_users(uuids: list[int]) -> list[Coroutine[int, Any, dict]]:
    return [get_user_from_db(pk) for pk in uuids]


@async_timed()
async def main(users: Coroutine[list[int], Any, list[Coroutine[int, Any, dict]]]):
    users_ = [user for user in await users]
    result = await asyncio.gather(*users_)
    return result


if __name__ == '__main__':
    r = asyncio.run(main(get_users([1, 2, 3])))
    print(r)