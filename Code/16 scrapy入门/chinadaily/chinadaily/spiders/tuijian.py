import scrapy
from ..items import ChinadailyItem


class TuijianSpider(scrapy.Spider):
    name = 'tuijian'
    allowed_domains = ['chinadaily.com.cn']
    start_urls = [f'http://language.chinadaily.com.cn/thelatest/page_{page}.html' for page in range(1, 11)]

    def parse(self, response):
        # print(response.text)
        divs = response.xpath('//div[@class="gy_box"]')
        for div in divs:
            img_url = 'http:' + div.xpath('.//a/img/@src').get()
            title = div.xpath('.//div/p[1]/a/text()').get().strip()
            intro = div.xpath('.//div/p[2]/a/text()').get().strip()
            # print(img_url, title, intro)
            yield ChinadailyItem(title=title, intro=intro, img_url=img_url)
