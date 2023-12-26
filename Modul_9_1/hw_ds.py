import requests
from bs4 import BeautifulSoup
import json


def get_page_content(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def get_quotes(soup):
    quotes = soup.select('div.quote')
    return [{'text': quote.select_one('span.text').text,
             'author': quote.select_one('small.author').text} for quote in quotes]


def get_authors(soup):
    authors = soup.select('div.quote small.author')
    return list(set([author.text for author in authors]))


def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def main():
    base_url = 'http://quotes.toscrape.com'
    page = get_page_content(base_url)
    quotes = get_quotes(page)
    authors = get_authors(page)

    save_to_json(quotes, 'quotes.json')
    save_to_json(authors, 'authors.json')

    while True:
        next_page_link = page.select_one('li.next > a')
        if not next_page_link:
            break
        next_page_url = base_url + next_page_link['href']
        page = get_page_content(next_page_url)
        quotes.extend(get_quotes(page))
        authors.extend(get_authors(page))

    save_to_json(quotes, 'quotes.json')
    save_to_json(authors, 'authors.json')


if __name__ == '__main__':
    main()