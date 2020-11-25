"""
1. 采集网址 https://www.zhihu.com/people/ponyma/followers

2. 采集目标
    - 从马**腾的粉丝信息开始, 采集前十页数据
    - 需要粉丝的昵称和粉丝头像的url地址
    - 用正则表达式采集
"""

import requests
import re
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'authority': 'www.zhihu.com',
}
for page in range(1, 11):
    # 请求数据
    url = 'https://www.zhihu.com/people/ponyma/followers'
    params = {
        'page': page,
    }
    response = requests.get(url=url, headers=headers, params=params)
    response.encoding = response.apparent_encoding

    # 解析数据，通过网页分析，正则表达式如下
    infos = re.findall('"id":".*?","urlToken":".*?","name":"(.*?)","useDefaultAvatar":.*?,"avatarUrl":"(.*?)",',
                       response.text, re.S)

    for name, url in infos:
        # url = url.replace('\\u002F', '\\')
        url = url.encode().decode('unicode_escape')  # encode() 把数据以二进制编码 decode('unicode_escape')  指定解码
        print(name, url)

    print('-' * 100)

