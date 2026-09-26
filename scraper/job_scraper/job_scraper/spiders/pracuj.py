import json
import scrapy
from job_scraper.items import JobScraperItem


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
        for offer in offers:
            job_item = JobScraperItem(
                title=offer.get("jobTitle"),
                company=offer.get("companyName"),
                location=offer.get("displayWorkplace"),
                skills=offer.get("technologies", []),
                url=offer.get("offerAbsoluteUri"),
                description=offer.get("jobDescription"),
                posted_at=offer.get("initialPublicated"),
                expire_at=offer.get("expirationDate"),
                salary=offer.get("salaryDisplayText"),
            )
            print(job_item)
            yield job_item
