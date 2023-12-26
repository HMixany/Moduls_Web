import requests
from bs4 import BeautifulSoup

	
def parse_laptops(response):
	soup = BeautifulSoup(response.text, "html.parser")
	laptops = soup.find_all("div", {"class": "goods-tile__inner"})
	
	for laptop in laptops:
		title = laptop.find_all("span", {"class": "goods-tile__title"})[0]
		price = laptop.find_all("span", {"class": "goods-tile__price-value"})[0]
		print(f"{title.get_text()} - {price.get_text()}")


base_url = ''
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

total_pages = soup.find_all("a", {"class": "pagination__link ng-star-inserted"})[-1]
total_pages = int(total_pages.get_text())

for n in range(1, total_pages):
	print(f"Scraping page $ {n}")
	next_page = f"{base_url}/page={n}/"
	response = requests.get(next_page)
	parse_laptops(response)
	