import json
import scrapy


class PracujSpider(scrapy.Spider):
    name = "pracuj"
    allowed_domains = ["pracuj.pl"]
    start_urls = ["https://it.pracuj.pl/praca/warszawa;wp?rd=30&et=1%2C17&itth=33%2C37"]

    def parse(self, response):
        data = response.css("script#__NEXT_DATA__::text").get()
        parsed_data = json.loads(data)
        offers = parsed_data["props"]["pageProps"]["dehydratedState"]["queries"][0][
            "state"
        ]["data"]["groupedOffers"]

        print(offers)
