# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import faker
import requests


def get_cookies():
    url = 'https://www.lagou.com/jobs/list_python'
    headers = {
        'referer': 'https://www.lagou.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    params = {
        'labelWords': '',
        'fromSearch': 'true',
        'suginput': '',

    }
    response = requests.get(url=url, params=params, headers=headers)
    cookies = response.cookies.get_dict()
    return cookies


class HeadersDownloaderMiddleware:

    def process_request(self, request, spider):
        """可以拿到请求体"""
        fake = faker.Faker()
        request.headers.update({
            'user-agent': fake.user_agent(),
            'origin': 'https://www.lagou.com',
            'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        })
        return None


class CookiesDownloaderMiddleware:
    """cookies中间件"""

    def process_request(self, request, spider):
        """可以拿到请求体"""
        fake = faker.Faker()
        request.cookies.update(get_cookies())
        return None
