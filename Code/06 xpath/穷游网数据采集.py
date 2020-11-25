"""
    目标网址: https://place.qyer.com/china/citylist-0-0-1/
    
    需求:
        1、用xpath采集数据
        2、采集以下信息
            city_name   # 城市名
            travel_people  # 去过的人数
            travel_hot    # 热门景点
            img_url  # 城市图片url
            
        解析到数据用print()函数打印即可
请在下方编写代码：
"""

import requests
import parsel

# 请求数据
url = 'https://place.qyer.com/china/citylist-0-0-1/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'authority': 'place.qyer.com'
}

res = requests.get(url=url, headers=headers)
res.encoding = res.apparent_encoding

# 解析数据
selector = parsel.Selector(res.text)
lis = selector.xpath('//ul[@class="plcCitylist"]/li')

for li in lis:
    city_name = li.xpath('.//h3/a/text()').get()
    travel_people = li.xpath('.//p[2]/text()').get()
    travel_hot = li.xpath('.//p[3]//a/text()').getall()
    img_url = li.xpath('.//p[1]/a/img/@src').get()
    travel_hot = [x.strip() for x in travel_hot]
    print(city_name, travel_people, ','.join(travel_hot), img_url)
