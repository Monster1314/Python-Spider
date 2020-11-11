import requests
import parsel
import time

url = 'https://movie.douban.com/top250'
headers = {
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
for num in range(0, 226, 25):
    params = {
        'start': num,
        'filter': ''
    }
    response = requests.get(url=url, headers=headers, params=params)
    response.encoding = response.apparent_encoding
    selector = parsel.Selector(response.text)
    titles = selector.css('div.hd span:nth-child(1)::text').getall()
    infos = selector.css('div.info div.bd p::text').getall()
    scores = selector.css('div.star span.rating_num::text').getall()
    follows = selector.css('div.star span:nth-child(4)::text').getall()
    for i in range(len(titles)):
        print(titles[i], infos[i].strip(), scores[i], follows[i])
    print('-'*100)
    time.sleep(2)
