"""
    请求拉勾网 python 前三页的招聘数据，
    (温馨提示：速度不要太快，小心被封)

    需求：
        获取以下字段信息，用print（）函数打印即可
        'city': 城市
        'companyFullName': 公司名
        'companySize': 公司规模
        'education': 学历
        'positionName': 职位名称
        'salary': 薪资
        'workYear': 工作时间
"""

import requests
import time


def get_cookies():
    '''获取当前的cookies'''
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
    cookies = response.cookies.get_dict()
    return cookies


def get_info(cookies, data):
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

    response = requests.post(url=url, headers=headers, params=params, data=data, cookies=cookies)
    
    # 解析数据
    ls = response.json()['content']['positionResult']['result']
    for work in ls:
        print(work["city"], work["companyFullName"], work["companySize"], work["education"], work["positionName"], work["salary"], work["workYear"])

    show_id = response.json()['content']['showId']
    return show_id


if __name__ == '__main__':
    origin_data = {
        'first': 'true',
        'pn': '1',
        'kd': 'python',
        'sid': '',
    }
    for page in range(1, 4):
        print(f'第{page}页职位信息')
        cookie = get_cookies()
        sid = get_info(cookie, data=origin_data)
        origin_data.update({
            'sid': sid,
            'first': 'false',
            'pn': page + 1,
        })
        print('-'*100)
        time.sleep(2)  # 延时，避免给服务器造成太大压力
