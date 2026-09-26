# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass
from datetime import datetime


@dataclass
class JobScraperItem:
    title: str
    company: str
    location: str
    skills: list[str]
    url: str
    description: str
    posted_at: datetime
    expire_at: datetime
    salary: str | None
