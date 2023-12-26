import requests
import json
from bs4 import BeautifulSoup

base_url = 'https://quotes.toscrape.com/'
# Спочатку треба скрапити сторінку за допомогою модуля requests
# response = requests.get('https://quotes.toscrape.com/')
# print(response.text)

# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
# print(soup.title.string)
# print(soup.find_all('span', attrs={'class': 'text'}))
# result = []
# quotes_spans = soup.find_all('span', attrs={'class': 'text'})
# for quote_span in quotes_spans:
#     print(quote_span.string)
#     result.append({'quote': quote_span.string})
# print(result)
print('==============================================================')
# quotes_divs = soup.find_all('div', attrs={'class': 'quote'})
# for quote_div in quotes_divs:
#     tags = []
#     quote_span = quote_div.find('span', attrs={'class': 'text'})
#     author = quote_div.find('small', attrs={'class': 'author'})
#     tags_a = quote_div.find_all('a', attrs={'class': 'tag'})
#     for tag in tags_a:
#         tags.append(tag.string)
#     print(quote_span.string)
#     print(author.string)
#     print(tags)
#     result.append({'quote': quote_span.string, 'author': author.string, 'tags': tags})
# with open('quotes.json', 'w') as fh:
#     json.dump(result, fh)


def parse_quotes(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []
    authors_href = []
    quotes_divs = soup.find_all('div', attrs={'class': 'quote'})
    for quote_div in quotes_divs:
        tags = []
        quote_span = quote_div.find('span', attrs={'class': 'text'})
        author_name = quote_div.find('small', attrs={'class': 'author'})
        tags_a = quote_div.find_all('a', attrs={'class': 'tag'})
        for tag in tags_a:
            tags.append(tag.string)
        print(quote_span.string)
        print(author_name.string)
        print(tags)
        quotes.append({'quote': quote_span.string, 'author': author_name.string, 'tags': tags})
        authors_url = base_url + quote_div.find("a").get("href")
        authors_href.append(authors_url)
    return quotes, authors_href


def parse_authors(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    author_fullname = soup.find('h3', attrs={'class': 'author-title'}).string
    born_date = soup.find('span', attrs={'class': 'author-born-date'}).string
    born_location = soup.find('span', attrs={'class': 'author-born-location'}).string
    description = soup.find('div', attrs={'class': 'author-description'}).string
    result = {
        "fullname": author_fullname, "born_date": born_date, "born_location": born_location, "description": description
    }
    return result


if __name__ == '__main__':
    result_by_quotes = []
    result_by_authors = []
    authors_urls = []
    response = requests.get(base_url)
    result_by_quotes.extend(parse_quotes(response))
    for n in range(2, 11):
        next_page = f"{base_url}/page/{n}/"
        response = requests.get(next_page)
        quotes_data, authors = parse_quotes(response)
        authors_urls.extend(authors)
        result_by_quotes.extend(quotes_data)

    authors_urls = list(set(authors_urls))
    for author_url in authors_urls:
        response = requests.get(author_url)
        result_by_authors.append(parse_authors(response))

    with open('quotes.json', 'w') as fh:
        json.dump(result_by_quotes, fh)

    with open('authors.json', 'w') as fh:
        json.dump(result_by_authors, fh)
