import requests
import pprint

url = 'https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76'
response = requests.get(url=url)
response.encoding = response.apparent_encoding
data = response.json()['data']
# print(type(data[0]))
# pprint.pprint(response.json()['data'])

for i in range(len(data)):
    print('title:', data[i]['title'], 'picPath:', data[i]['picPath'], 'playUrl:', data[i]['playUrl'])
