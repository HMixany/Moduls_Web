import asyncio
from concurrent.futures import ThreadPoolExecutor

import requests


from libs import async_timed, sync_timed

urls = [
    "https://fcdnipro.com", "https://github.com", "https://www.codewars.com", "https://rezka.cc/", "https://hltv.org/",
    "https://app.amplitude.com", "https://www.google.com", "https://www.python.org", "https://www.youtube.com/",
    "https://tabletki.ua", "https://app.tabnine.com/", "https://chat.openai.com/"
]


def get_preview(url: str):
    r = requests.get(url)
    return url, r.text[:100]