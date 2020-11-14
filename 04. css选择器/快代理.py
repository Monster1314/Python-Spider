"""
    使用 css 选择器将快代理中我需要的信息提取出来。
    目标网址：https://www.kuaidaili.com/free/
    
    需要解析以下数据:
        ip、
        port、
        类型

    提取出来print（）打印即可
    温馨提示: 爬取速度不要太快,加延迟,避免被封导致以后请求不到数据!
"""

import requests
import parsel
import time

for page in range(1, 4):
    # 请求数据
    url = f'https://www.kuaidaili.com/free/inha/{page}/'
    headers = {
        'Host': 'www.kuaidaili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    
    # 解析数据
    selector = parsel.Selector(response.text)

    ips = selector.css('table.table.table-bordered.table-striped tbody tr td:nth-child(1)::text').getall()
    ports = selector.css('table.table.table-bordered.table-striped tbody tr td:nth-child(2)::text').getall()
    kinds = selector.css('table.table.table-bordered.table-striped tbody tr td:nth-child(4)::text').getall()
    for i in range(len(ips)):
        print(ips[i], ports[i], kinds[i])
    print('-'*100)
    time.sleep(2)
