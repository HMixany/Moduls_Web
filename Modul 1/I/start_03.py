import requests


class ApiClient:
    def __init__(self, fetch: requests):
        self.fetch = fetch

    def get_json(self, url: str):
        response = self.fetch.get(url)
        return response.json()

    def pretty_view(self, data: list[dict]):
        result = [
            {
                f"{el.get('ccy')})": {
                    "buy": float(el.get("buy")),
                    "sale": float(el.get("sale")),
                }
            }
        ]
