import httpx
import asyncio
import platform


class HttpError(Exception):
    pass


async def request(url: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        if r.status_code == 200:
            result = r.json()
            return result
        else:                                                 # обробка помилки 404
            raise HttpError(f"Error status: {r.status_code} for {url}")


async def main():
    try:
        respons = await request('https://api.privatbank.ua/p24api/exchange_rates?date=01.12.2014')
        return respons
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)