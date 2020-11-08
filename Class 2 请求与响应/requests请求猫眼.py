"""
    目标地址：https://maoyan.com/board/4?offset=0

    要求：
    1、请求到目标网址数据，需要在请求到的数据中看到当前页面所有的电影名字、主演、上映时间、评分等信息
    2、请列举在请求不到数据时，需要添加几个常见请求头字段（课程讲过）
    请在下方编写代码
"""

import requests
import re

url = 'https://maoyan.com/board/4?offset=0'
headers = {
    'Host': 'maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 ',

}

response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding


names = re.findall('<p class="name"><a href=".*?" title="(.*?)" data-act="boarditem-click" data-val=".*?">.*?</a></p>',
                   response.text, re.S)
stars = re.findall('<p class="star">(.*?)</p>', response.text, re.S)
release_times = re.findall('<p class="releasetime">(.*?)</p>', response.text, re.S)
scores = re.findall('<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>',
                    response.text, re.S)
splice_score = [x + y for x, y in scores]

for i in range(len(names)):
    print(names[i], stars[i].strip(), release_times[i], splice_score[i])
