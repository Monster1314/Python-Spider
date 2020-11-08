# coding=utf-8

'''
    目标网址：https://index.mysteel.com/price/indexPrice.html
    选择8.1-11.1 广州，螺纹钢，HRB400-20MM
    爬取所有数据
'''

import requests
import json
import re
import csv
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'Referer': 'https://index.mysteel.com/',
    'Host': 'openapi.mysteel.com',
}

url = 'https://openapi.mysteel.com/zs/newprice/getChartMultiCity.ms'

params = {
    "callback": "callback",
    "catalog": "%E8%9E%BA%E7%BA%B9%E9%92%A2_:_%E8%9E%BA%E7%BA%B9%E9%92%A2",
    "city": "%E5%B9%BF%E5%B7%9E",
    "spec": "HRB400%2020MM_:_HRB400_20MM",
    "startTime": "2020-08-01",
    "endTime": "2020-11-01",
    "_": "1604721785488",
}

res = requests.get(url=url, headers=headers, params=params)
# print(res.text)

result = re.findall('callback\((.*?)\)', res.text, re.S)
json_data = json.loads(result[0])

title = json_data['title']

with open(title + '.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_writer = csv.DictWriter(f, fieldnames=['lineName', 'date', 'value'])
    csv_writer.writeheader()

    city_name = json_data['data'][0]['lineName']
    for data in json_data['data'][0]['dateValueMap']:
        data['lineName'] = city_name
        csv_writer.writerow(data)
