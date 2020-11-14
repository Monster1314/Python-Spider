"""
	目标网址：https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76
	
	要求：
		1、请求上述网址的数据
		2、把获取到的数据保存到json文件中
            文件命名: data.json
            需要在文件中看到json字符串
			
请在下方编写代码
"""

import requests
import json
import parsel

# 请求数据
url = "https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76"
res = requests.get(url=url).text

# 解析数据
content = json.dumps(res, ensure_ascii=False)  # .dumps()将字符串转换成对象; ensure_ascii=False确保中文不乱码
print(content)


# 保存数据
with open('data.json', mode='w', encoding='utf-8') as f:
    f.write(content)
