# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import csv


class CsvPipeline:
    """保持csv"""

    def __init__(self):
        """初始化方法"""
        self.f = open('douban.csv', mode='a', encoding='utf-8', newline='')
        self.csv_writer = csv.DictWriter(self.f, fieldnames=['title', 'info', 'score', 'comment',
                                                             'quote'])
        self.csv_writer.writeheader()

    def process_item(self, item, spider):
        """
        专门用来处理item数据
        :param item: 爬虫返回数据结构
        :param spider: 爬虫对象
        :return: item 必须原路返回
        """
        data = dict(item)
        self.csv_writer.writerow(data)
        return item

    def close_spider(self):
        """整个scrapy项目停止之前会调用的一个方法"""
        self.f.close()
