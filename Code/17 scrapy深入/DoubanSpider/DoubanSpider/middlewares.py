# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import faker


class DoubanspiderDownloaderMiddleware:

    def process_request(self, request, spider):
        fake = faker.Faker()
        request.headers.update({
            'user-agent': fake.user_agent(),
            'origin': 'movie.douban.com',
            'referer': 'Referer: https://movie.douban.com/top250?start=25&filter=',
        })
        return None
