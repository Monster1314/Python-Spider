"""
    目标网址: http://www.win4000.com/meinvtag17_1.html
    
    需求:
        影视图片大全文字下面有很多影视图集
        1、用xpath采集数据
        2、采集以下信息
            采集影视图集的标题
            采集影视图集中图片对应的url地址
            
        解析到数据用print()函数打印即可
请在下方编写代码：
"""

import requests
import parsel

url = 'http://www.win4000.com/meinvtag17_1.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'Host': 'www.win4000.com'
}
res = requests.get(url=url, headers=headers)
res.encoding = res.apparent_encoding
selector = parsel.Selector(res.text)
lis = selector.xpath('//div[@class="w1180 clearfix"]/div/div/div[2]/div/div/ul/li')
for li in lis:
    title = li.xpath('.//a/p/text()').get()
    img_url = li.xpath('.//a/img/@src').get()
    print(title, img_url)
