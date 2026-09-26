# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime


class JobScraperPipeline:
    def process_item(self, item):
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()

        for field_name in field_names:

            if field_name == "skills":
                skills = adapter.get(field_name)
                adapter[field_name] = [skill.lower() for skill in skills]

            if field_name == "posted_at" or field_name == "expire_at":
                value = adapter.get(field_name)
                adapter[field_name] = datetime.fromisoformat(value)
        return item
