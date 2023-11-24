import asyncio
from concurrent.futures import ThreadPoolExecutor

import requests
from requests.exceptions import InvalidSchema, MissingSchema, SSLError

from timing import async_timed

urls = [
    "https://fcdnipro.com", "https://github.com", "https://www.codewars.com", "https://rezka.cc/", "https://hltv.org/",
    "https://app.amplitude.com", "https://www.google.com", "https://www.python.org", "https://www.youtube.com/",
    "https://tabletki.ua", "https://app.tabnine.com/", "https://chat.openai.com/",
]


def get_preview(url: str):
    r = requests.get(url)
    return url, r.text[:100]


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(10) as pool:
        futures = [loop.run_in_executor(pool, get_preview, url) for url in urls]
        done, pending = await asyncio.wait(futures, return_when=asyncio.FIRST_COMPLETED)
        print(f'Done: {done}')
        print(f'Pending: {pending}')
        [task.cancel() for task in pending]
        return done


if __name__ == '__main__':
    r: list = asyncio.run(main())
    print(r)
    g = [i ** 2 for i in range(10)]
    it = (i ** 2 for i in range(10))
    print(g)
    print(it)