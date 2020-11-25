# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    company_name = scrapy.Field()
    company_size = scrapy.Field()
    education = scrapy.Field()
    position_name = scrapy.Field()
    salary = scrapy.Field()
    work_year = scrapy.Field()

