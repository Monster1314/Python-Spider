"""
    使用 css 选择器将猫眼 100 十页全部电影信息全部提取出来。
    目标网址：https://maoyan.com/board/4
    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）

    提取出来print（）打印即可
    温馨提示: 爬取速度不要太快,加延迟,避免被封导致以后请求不到数据!
"""

import requests
import parsel
import time


url = 'https://maoyan.com/board/4'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'Host': 'maoyan.com',
    'Cookie': '__mta=209474477.1604202787584.1604202787584.1604203135623.2; uuid_n_v=v1; uuid=BEBCE5001BF511EB9E99A582304AF4155ADCF1479DB141F9A0A8BB08A10055D1; _csrf=1a3d3feb25a7bcadb7c93484cd4969e1653ed28dbc8bdd4537f50e54fe220b39; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1604202787; _lxsdk_cuid=17581b9f3cc5a-039de6ddc81ce8-303464-144000-17581b9f3cdc8; _lxsdk=BEBCE5001BF511EB9E99A582304AF4155ADCF1479DB141F9A0A8BB08A10055D1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1604203135; _lxsdk_s=17581ef6c55-5ae-ce7-746%7C%7C6'
}  # 这里的cookies是有时效的

for page in range(0, 91, 10):
    params = {
        'offset': page
    }
    # 请求数据
    response = requests.get(url=url, headers=headers, params=params)
    response.encoding = response.apparent_encoding
    
    # 解析数据
    selector = parsel.Selector(response.text)
    names = selector.css('p.name a::attr(title)').getall()
    stars = selector.css('p.star::text').getall()
    release_times = selector.css('p.releasetime::text').getall()
    scores = selector.css('p.score i::text').getall()

    for i in range(len(names)):
        print(names[i].strip(), stars[i].strip(), release_times[i], scores[2*i] + scores[2*i+1])

    print('-'*100)
    time.sleep(2)
