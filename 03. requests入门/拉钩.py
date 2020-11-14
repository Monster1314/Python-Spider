"""
    要求：
        1、能够在一个py文件下请求数据

        2、获取以下字段信息，用print（）函数打印即可
            'city': 城市
            'companyFullName': 公司名
            'companySize': 公司规模
            'education': 学历
            'positionName': 职位名称
            'salary': 薪资
            'workYear': 工作时间


请在下方编写代码
"""

import requests


def get_cookies():
    '''获取当前cookies，以便能够完成爬取过程'''
    url = 'https://www.lagou.com/jobs/list_python'
    headers = {
        'referer': 'https://www.lagou.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    params = {
        'labelWords': '',
        'fromSearch': 'true',
        'suginput': '',

    }
    response = requests.get(url=url, params=params, headers=headers)
    cookies = response.cookies.get_dict()  # 获取cookies
    return cookies


def get_info(cookies):
    # 请求数据
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    headers = {
        'origin': 'https://www.lagou.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'authority': 'www.lagou.com',
        'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    }
    params = {
        'needAddtionalResult': 'false',
    }
    data = {
        'first': 'true',
        'pn': '1',
        'kd': 'python',
        'sid': '',
    }
    response = requests.post(url=url, headers=headers, params=params, data=data, cookies=cookies)
    
    # 解析数据
    ls = response.json()['content']['positionResult']['result']
    for work in ls:
        print(work["city"], work["companyFullName"], work["companySize"], work["education"], work["positionName"], work["salary"], work["workYear"])


if __name__ == '__main__':
    cookie = get_cookies()
    get_info(cookie)
