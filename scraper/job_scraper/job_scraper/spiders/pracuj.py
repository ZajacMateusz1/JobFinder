import scrapy


class PracujSpider(scrapy.Spider):
    name = "pracuj"
    allowed_domains = ["pracuj.pl"]
    start_urls = ["https://www.pracuj.pl/"]

    def parse(self, response):
        print(response.text)
