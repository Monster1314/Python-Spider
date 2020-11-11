"""
一次性将一个系列图片全部爬取下来

请下下方开始编写代码
"""

import requests
import re
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
url = 'http://www.win4000.com/wallpaper_detail_174996.html'
response = requests.get(url=url, headers=headers)
num = re.findall('<div class="ptitle"><h1>鬼灭之刃热血酷炫动漫桌面壁纸</h1>（<span>1</span>/<em>(.*?)</em>）</div>', response.text, re.S)

for page in range(1, int(num[0])+1):
    page_url = f'http://www.win4000.com/wallpaper_detail_174996_{page}.html'
    res = requests.get(url=page_url, headers=headers)
    img_url = re.findall('<img class="pic-large" src="(.*?)" alt=".*?" title=".*?">', res.text, re.S)
    # print(img_url)

    name = img_url[0].split('/')[-1]
    img = requests.get(url=img_url[0], headers=headers).content
    with open(name, 'wb') as f:
        f.write(img)
    print('下载完成：', name)
