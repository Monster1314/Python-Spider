import scrapy
from scrapy import FormRequest
from ..items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = [f'https://movie.douban.com/top250?start={num}&filter=' for num in range(0, 251, 25)]
    # start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    def parse(self, response):
        # print(response.text)
        lis = response.css('.grid_view li')
        for li in lis:
            title = li.css('.hd a span::text').get()
            info = li.css('.bd p::text').get().strip().replace(' ', ' ')
            score = li.css('.bd div span:nth-child(2)::text').get()
            comment = li.css('.bd div span:nth-child(4)::text').get()
            quote = li.css('.quote span::text').get()
            # print(title, info, score, comment, quote)

            yield DoubanspiderItem(title=title, info=info, score=score, comment=comment, quote=quote)
