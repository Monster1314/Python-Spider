# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv


class ChinadailyPipeline:
    def process_item(self, item, spider):
        data = dict(item)
        with open('chinadaily.csv', mode='a', encoding='utf-8') as f:
            f.write(data['title'] + ',' + data['intro'] + ',' + data['img_url'])
            f.write('\n')
        return item
