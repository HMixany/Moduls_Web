from typing import Any, List, Dict

import requests


class ApiClient:
    def __init__(self, fetch: requests):
        self.fetch = fetch

    def get_json(self, url: str):
        response = self.fetch.get(url)
        return response.json()


class Viewer:
    def display(self, data: list[dict[str, Any]]):
        raise NotImplementedError


class CurrencyViewer(Viewer):
    def _adapter(self, data: list[dict[str, Any]]):
        result = [
            {
                f"{el.get('ccy')})": {
                    "buy": float(el.get("buy")),
                    "sale": float(el.get("sale")),
                }
            }
            for el in data
        ]
        # result - это преобразование данных
        return result

    def display(self, data: list[dict[str, Any]]):
        result = self._adapter(data)
        pattern = "|{:^10}|{:^10}|{:^10}|"
        print(pattern.format("currency", "sale", "buy"))
        for el in result:
            currency, *_ = el.keys()
            buy = el.get(currency).get("buy")
            sale = el.get(currency).get("sale")
            print(pattern.format(currency, sale, buy))


if __name__ == '__main__':
    api_client = ApiClient(requests)
    viewer = CurrencyViewer()
    data = api_client.get_json('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')
    viewer.display(data)
    # data = api_client.get_json('https://api.monobank.ua/bank/currency')
    # api_client.pretty_view(data)