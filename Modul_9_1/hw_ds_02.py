from bs4 import BeautifulSoup
import requests


def get_page_content(url):
    # Отримання вмісту сторінки
    # ...
    page_content = requests.get(url).text
    return BeautifulSoup(page_content, 'html.parser')


def get_quotes(soup):
    return [quote.text for quote in soup.find_all('div', class_='quote')]


def get_authors(soup):
    return [author.text for author in soup.find_all('small', class_='author')]


base_url = 'http://example.com'
page = get_page_content(base_url)
quotes = get_quotes(page)
authors = get_authors(page)

while True:
    next_page_link = page.find('li', class_='next').find('a')
    if not next_page_link:
        break
    next_page_url = base_url + next_page_link['href']
    page = get_page_content(next_page_url)
    quotes.extend(get_quotes(page))
    authors.extend(get_authors(page))