import scrapy


class QuotesSpider(scrapy.Spider):
	name = "quotes"
	
	def start_requests(self):
		urls = [
		"https://quotes.toscrapy.com/page/1/",
		"https://quotes.toscrapy.com/page/2/",
		"https://quotes.toscrapy.com/page/3/"
		]
		
		for url in urls:
			yield scrapy.Request(url=url)
			
	def parse(self, response):
		page_n = response.url.split("/")[-2]
		
		with open(f"{page_n}.html", "w", encoding="utf-8") as file:
			file.write(response.body.decode())