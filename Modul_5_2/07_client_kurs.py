import aiohttp
import asyncio
import platform


class HttpError(Exception):
    pass


async def request(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    return result
                else:                                                 # обробка помилки 404
                    raise HttpError(f"Error status: {resp.status} for {url}")
        except (aiohttp.ClientConnectorError, aiohttp.InvalidURL) as err:  # обробка інших помилок
            raise HttpError(f'Connection error: {url}', str(err))


async def main():
    try:
        respons = await request('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
        return respons
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)