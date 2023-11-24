import asyncio
from concurrent.futures import ThreadPoolExecutor

import requests
from requests.exceptions import InvalidSchema, MissingSchema, SSLError

from libs import async_timed, sync_timed

urls = [
    "https://fcdnipro.com", "https://github.com", "https://www.codewars.com", "https://rezka.cc/", "https://hltv.org/",
    "https://app.amplitude.com", "https://www.google.com", "https://www.python.org", "https://www.youtube.com/",
    "https://tabletki.ua", "https://app.tabnine.com/", "https://chat.openai.com/", "hgjk", "ws://jhkgkg.com",
]


def get_preview(url: str):
    r = requests.get(url)
    return url, r.text[:100]


@sync_timed()
def main_sync():
    results = []
    for url in urls:
        try:
            results.append(get_preview(url))
        except (InvalidSchema, MissingSchema, SSLError) as err:
            print(err)
    return results


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(10) as pool:
        futures = [loop.run_in_executor(pool, get_preview, url) for url in urls]
        r = await asyncio.gather(*futures, return_exceptions=True)  # return_exceptions=True помилки додає теж до списку
        return r


if __name__ == '__main__':
    print(main_sync())
    print(asyncio.run(main()))
    r: list = asyncio.run(main())
    # видалимо помилки з списку

    r_new = list(filter(lambda el: not isinstance(el, Exception), r))
    print(r_new)