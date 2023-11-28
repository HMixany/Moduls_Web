import sys
import httpx
import asyncio
import platform
from datetime import datetime, timedelta


class HttpError(Exception):
    pass


async def request(url: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(url, timeout=20)
        if r.status_code == 200:
            result = r.json()
            return result
        else:                                                 # обробка помилки 404
            raise HttpError(f"Error status: {r.status_code} for {url}")


async def choise(data: dict, currency: str):
    await asyncio.sleep(0)
    dict = list(filter(lambda x: x.get('currency') == currency, data['exchangeRate']))[0]
    return {'sale': dict.get('saleRate'), 'purchase': dict.get('purchaseRate')}


async def data_adapter(data: dict):
    eur_dict = await choise(data, 'EUR')
    usd_dict = await choise(data, 'USD')
    return {data['date']: {'EUR': eur_dict, 'USD': usd_dict}}


async def main(delta_day):
    result = []
    today = datetime.now()
    current_day = today - timedelta(days=int(delta_day))
    try:
        while current_day != today:
            shift = current_day.strftime("%d.%m.%Y")
            respons = await request(f'https://api.privatbank.ua/p24api/exchange_rates?date={shift}')
#             respons = s = {'date': '01.12.2014','bank': 'PB','baseCurrency': 980,'baseCurrencyLit': 'UAH','exchangeRate': [
#         {'baseCurrency': 'UAH', 'currency': 'AUD', 'saleRateNB': 12.831925, 'purchaseRateNB': 12.831925},
#         {'baseCurrency': 'UAH', 'currency': 'CAD', 'saleRateNB': 13.21074, 'purchaseRateNB': 13.21074, 'saleRate': 15.0, 'purchaseRate': 13.0},
#         {'baseCurrency': 'UAH', 'currency': 'CZK', 'saleRateNB': 0.679695, 'purchaseRateNB': 0.679695, 'saleRate': 0.8, 'purchaseRate': 0.6},
#         {'baseCurrency': 'UAH', 'currency': 'DKK', 'saleRateNB': 2.525893, 'purchaseRateNB': 2.525893},
#         {'baseCurrency': 'UAH', 'currency': 'HUF', 'saleRateNB': 0.0612592, 'purchaseRateNB': 0.0612592},
#         {'baseCurrency': 'UAH', 'currency': 'ILS', 'saleRateNB': 3.862738, 'purchaseRateNB': 3.862738, 'saleRate': 4.5, 'purchaseRate': 3.7},
#         {'baseCurrency': 'UAH', 'currency': 'JPY', 'saleRateNB': 0.1272593, 'purchaseRateNB': 0.1272593, 'saleRate': 0.15, 'purchaseRate': 0.12},
#         {'baseCurrency': 'UAH', 'currency':'LVL', 'saleRateNB': 0.1272593, 'purchaseRateNB': 0.1272593},
#         {'baseCurrency': 'UAH', 'currency': 'LTL', 'saleRateNB': 5.443385, 'purchaseRateNB': 5.443385},
#         {'baseCurrency': 'UAH', 'currency': 'NOK', 'saleRateNB': 2.160957, 'purchaseRateNB': 2.160957, 'saleRate': 2.6, 'purchaseRate': 2.1},
#         {'baseCurrency': 'UAH', 'urrncy': 'SKK', 'saleRateNB': 2.160957, 'purchaseRateNB': 2.160957},
#         {'baseCurrency': 'UAH', 'currency': 'SEK', 'saleRateNB': 2.028375, 'purchaseRateNB': 2.028375},
#         {'baseCurrency': 'UAH', 'currency': 'CHF', 'saleRateNB': 15.638975, 'purchaseRateNB': 15.638975, 'saleRate': 17.0, 'purchaseRate': 15.5},
#         {'baseCurrency': 'UAH', 'currency': 'GBP', 'saleRateNB': 23.632491, 'purchaseRateNB': 23.632491, 'saleRate': 25.8, 'purchaseRate': 24.0},
#         {'baseCurrency': 'UAH', 'currency': 'USD', 'saleRateNB': 15.056413, 'purchaseRateNB': 15.056413, 'saleRate': 15.7, 'purchaseRate': 15.35},
#         {'baseCurrency': 'UAH', 'currency': 'BYR', 'saleRateNB': 0.00139, 'purchaseRateNB': 0.00139},
#         {'baseCurrency': 'UAH', 'currency': 'EUR', 'saleRateNB': 18.79492, 'purchaseRateNB': 18.79492, 'saleRate': 20.0, 'purchaseRate': 19.2},
#         {'baseCurrency': 'UAH', 'currency': 'GEL', 'saleRateNB': 8.150089, 'purchaseRateNB': 8.150089},
#         {'baseCurrency': 'UAH', 'currency': 'PLZ', 'saleRateNB': 4.492201, 'purchaseRateNB': 4.492201, 'saleRate': 5.0, 'purchaseRate': 4.2}
#     ]
# }
            result.append(await data_adapter(respons))
            current_day = current_day + timedelta(days=1)
        return result
        # respons = await request(f'https://api.privatbank.ua/p24api/exchange_rates?date=01.12.2014')
        # return respons
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main(sys.argv[1]))
    print(r)