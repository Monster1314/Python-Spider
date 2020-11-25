import scrapy
from scrapy import FormRequest
from ..items import LagouspiderItem


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    # start_urls = ['http://lagou.com/']

    def start_requests(self):
        yield FormRequest(
            url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',
            formdata={
                'first': 'true',
                'pn': '1',
                'kd': 'python',
            },
            callback=self.parse,
            meta={'page': 1}
        )

    def parse(self, response):
        # print(response.json())
        # print(response.request.headers)
        json_data = response.json()['content']['positionResult']['result']
        # print(json_data)
        for data in json_data:
            city = data['city']
            company_name = data['companyFullName']
            company_size = data['companyFullName']
            education = data['education']
            position_name = data['positionName']
            salary = data['salary']
            work_year = data['workYear']
            # print(city)
            yield LagouspiderItem(city=city, company_name=company_name, company_size=company_size, education=education,
                                  position_name=position_name, salary=salary, work_year=work_year)

        sid = response.json()['content']['showId']
        page = response.meta.get('page')

        if page <= 10:
            yield FormRequest(
                url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',
                formdata={
                    'first': 'false',
                    'pn': str(page + 1),
                    'kd': 'python',
                    'sid': str(sid),
                },
                callback=self.parse,
                meta={'page': page + 1}
            )
