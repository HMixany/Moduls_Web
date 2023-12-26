import requests
from bs4 import BeautifulSoup

base_url = ''
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")
quotes_divs = soup.find_all("div", {"class": "quote"})
authors_urls = []
for quote_div in quotes_divs:
	author_name = quote_div.find("small", attrs={"class": "author"}).string
	authors_url = base_url + quote_div.find("a").get("href")
	authors_urls.append(authors_url)
	response = requests.get(authors_url)
	soup = BeautifulSoup(response.text, "html.parser")
	
for authors_url in authors_urls:
	response = requests.get(authors_url)
	soup = BeautifulSoup(response.text, "html.parser")
	