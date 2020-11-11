"""
    目标网址: https://nba.hupu.com/stats/players/pts
    
    需求:
        1、用xpath采集nba球员数据（三页）
        2、采集以下信息
            rank   # 排名
            player  # 球员
            team    # 球队
            score    # 得分
            hit_shot   # 命中-出手
            hit_rate   # 命中率
            hit_three   # 命中-三分
            three_rate   # 三分命中率
            hit_penalty   # 命中-罚球
            penalty_rate   # 罚球命中率
            session   # 场次
            playing_time   # 上场时间
            
        解析到数据用print()函数打印即可
请在下方编写代码：
"""

import requests
import parsel

url = 'https://nba.hupu.com/stats/players/pts'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'authority': 'nba.hupu.com',
}

res = requests.get(url=url, headers=headers)
res.encoding = res.apparent_encoding
selector = parsel.Selector(res.text)
lis = selector.xpath('//tbody/tr')

print('排名 球员 球队 得分 命中-出手 命中率 命中-三分 三分命中率 命中-罚球 罚球命中率 场次 上场时间')
for li in lis[1:]:
    rank = li.xpath('.//td[1]/text()').get()
    player = li.xpath('.//td[2]/a/text()').get()
    team = li.xpath('.//td[3]/a/text()').get()
    score = li.xpath('.//td[4]/text()').get()
    hit_shot = li.xpath('.//td[5]/text()').get()
    hit_rate = li.xpath('.//td[6]/text()').get()
    hit_three = li.xpath('.//td[7]/text()').get()
    three_rate = li.xpath('.//td[8]/text()').get()
    hit_penalty = li.xpath('.//td[9]/text()').get()
    penalty_rate = li.xpath('.//td[10]/text()').get()
    session = li.xpath('.//td[11]/text()').get()
    playing_time = li.xpath('.//td[12]/text()').get()
    print(rank, player, team, score, hit_shot, hit_rate, hit_three, three_rate, hit_penalty, penalty_rate, session, playing_time, sep='\t')
