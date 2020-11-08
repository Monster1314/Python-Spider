"""
表情包爬取
将此页面下的前十页图片全部获取下来：https://fabiaoqing.com/biaoqing

清下下方开始编写代码
"""

import requests
import re


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}

for page in range(1, 11):
    page_url = 'https://fabiaoqing.com/biaoqing/lists/page/{}.html'.format(page)
    origin_url = 'https://fabiaoqing.com/'
    res = requests.get(url=page_url, headers=headers)
    res.encoding = res.apparent_encoding

    '<img class="ui image lazy" data-original="(.*?)" src=".*?" title=".*?" alt=".*?"'
    data_list = re.findall('<img class="ui image lazy" data-original="(.*?)" src=".*?" title=".*?" alt=".*?"', res.text, re.S)
    # print(data_list)
    for url in data_list:
        url = url.replace('bmiddle', 'large')
        img = requests.get(url=url, headers=headers).content
        name = url.split('/')[-1]
        with open(name, mode='wb') as f:
            f.write(img)
        print('下载完成：', name)
