import re
import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://index.minfin.com.ua/ua/russian-invading/casualties/'


def get_urls():
    urls = ["/"]
    html_doc = requests.get(BASE_URL)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    content = soup.select('div[class=ajaxmonth] h4[class=normal] a')
    prefix = '/month.php?month='
    for link in content:
        url = prefix + re.search(r'\d{4}-\d{2}', link['id']).group()
        urls.append(url)
    return urls


def spider(url):
    result = []
    html_doc = requests.get(BASE_URL + url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    content = soup.select('ul[class=see-also] li[class=gold]')
    for li in content:
        parse_elements = {}
        date_key = li.find('span', attrs={'class': 'black'}).text
        try:
            date_key = datetime.strptime(date_key, '%d.%m.%Y').isoformat()
        except ValueError:
            print(f'Error for {date_key}')
            continue
        parse_elements.update({'date': date_key})
        losses = li.find('div', attrs={'class': 'casualties'}).find('div').find('ul')
        for loss in losses:
            name, quantity, *_ = loss.text.split('—')
            name = name.strip()
            quantity = re.search(r'\d+', quantity).group()
            parse_elements.update({name: int(quantity)})
        result.append(parse_elements)
    return result


def main(urls):
    data = []
    for url in urls:
        data.extend(spider(url))
    return data


if __name__ == '__main__':
    print(result := main(get_urls()))
    with open('kacapy.json', 'w', encoding='utf-8') as fh:
        json.dump(result, fh, ensure_ascii=False, indent=2)

