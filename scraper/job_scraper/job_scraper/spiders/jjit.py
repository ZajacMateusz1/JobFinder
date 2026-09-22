import scrapy


class JjitSpider(scrapy.Spider):
    name = "jjit"
    allowed_domains = ["justjoin.it"]
    start_urls = ["https://justjoin.it/"]

    def parse(self, response):
        pass
