import requests
import parsel
import time

for page in range(1, 4):
    url = f'https://www.kuaidaili.com/free/inha/{page}/'
    headers = {
        'Host': 'www.kuaidaili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    selector = parsel.Selector(response.text)

    ips = selector.css('table.table.table-bordered.table-striped tbody tr td:nth-child(1)::text').getall()
    ports = selector.css('table.table.table-bordered.table-striped tbody tr td:nth-child(2)::text').getall()
    kinds = selector.css('table.table.table-bordered.table-striped tbody tr td:nth-child(4)::text').getall()
    for i in range(len(ips)):
        print(ips[i], ports[i], kinds[i])
    print('-'*100)
    time.sleep(2)
