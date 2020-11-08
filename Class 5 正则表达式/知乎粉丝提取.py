import requests
import re
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'authority': 'www.zhihu.com',
}
for page in range(1, 11):
    url = 'https://www.zhihu.com/people/ponyma/followers'
    params = {
        'page': page,
    }
    response = requests.get(url=url, headers=headers, params=params)
    response.encoding = response.apparent_encoding
    # print(response.text)

    infos = re.findall('"id":".*?","urlToken":".*?","name":"(.*?)","useDefaultAvatar":.*?,"avatarUrl":"(.*?)",',
                       response.text, re.S)
    # print(infos)
    for name, url in infos:
        # url = url.replace('\\u002F', '\\')
        url = url.encode().decode('unicode_escape')  # encode() 把数据以二进制编码 decode('unicode_escape')  指定解码
        print(name, url)

    print('-' * 100)

